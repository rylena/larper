from __future__ import annotations

from dataclasses import asdict, dataclass
import re


@dataclass(frozen=True)
class TaskProfile:
    domain: str
    role: str
    subject: str
    quality_bar: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


_RULES: list[tuple[str, tuple[str, ...], str, str]] = [
    (
        "web_development",
        ("website", "landing page", "web app", "frontend", "ui", "ux"),
        "a world-class web designer and frontend developer with strong information architecture instincts",
        "Prioritize clean UX, strong structure, accessible copy, and polished visual hierarchy.",
    ),
    (
        "creative_writing",
        ("story", "poem", "novel", "script", "dialogue", "bedtime", "fiction"),
        "a world-class creative writer and storyteller with excellent command of tone, pacing, and imagery",
        "Prioritize originality, emotional resonance, memorable voice, and tight prose.",
    ),
    (
        "analysis",
        ("analyze", "analysis", "evaluate", "critique", "assess", "break down"),
        "a world-class analyst and strategic thinker who separates signal from noise",
        "Be rigorous, explicit about assumptions, and prioritize the most decision-relevant insights first.",
    ),
    (
        "marketing",
        ("marketing", "ad copy", "copywriting", "campaign", "headline", "brand"),
        "a world-class marketer and copywriter with strong positioning instincts",
        "Prioritize clarity, persuasion, audience fit, and concrete conversion-oriented messaging.",
    ),
    (
        "software_development",
        ("build", "code", "implement", "api", "python", "react", "bug", "refactor"),
        "a world-class software engineer who writes practical, correct, maintainable solutions",
        "Prioritize correctness, clear architecture, edge cases, and production-ready execution.",
    ),
]

_SUBJECT_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"\babout\s+(?P<subject>.+)$", re.IGNORECASE),
    re.compile(r"\bfor\s+(?P<subject>.+)$", re.IGNORECASE),
]


def normalize_request(user_request: str) -> str:
    text = user_request.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def extract_subject(user_request: str) -> str:
    text = normalize_request(user_request)
    for pattern in _SUBJECT_PATTERNS:
        match = pattern.search(text)
        if match:
            subject = match.group("subject").strip(" .!?")
            if subject:
                return subject
    return "the user\'s requested subject"


def classify_task(user_request: str) -> TaskProfile:
    text = normalize_request(user_request)
    lowered = text.lower()

    for domain, keywords, role, quality_bar in _RULES:
        if any(keyword in lowered for keyword in keywords):
            return TaskProfile(
                domain=domain,
                role=role,
                subject=extract_subject(text),
                quality_bar=quality_bar,
            )

    return TaskProfile(
        domain="general",
        role="a strong generalist problem solver who communicates clearly and reasons carefully",
        subject=extract_subject(text),
        quality_bar="Make reasonable assumptions, stay practical, and optimize for usefulness over flair.",
    )


def _capitalize_request(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        return stripped
    return stripped[0].upper() + stripped[1:]


def transform_prompt(user_request: str) -> str:
    request = normalize_request(user_request)
    profile = classify_task(request)
    task_sentence = _capitalize_request(request)
    if not task_sentence.endswith((".", "!", "?")):
        task_sentence += "."

    return (
        f"You are {profile.role}. "
        f"You are also deeply familiar with the subject matter for this task: {profile.subject}. "
        f"{task_sentence} "
        f"{profile.quality_bar} "
        "If important details are missing, make reasonable assumptions and state them briefly. "
        "Keep the response directly useful for the original request."
    )
