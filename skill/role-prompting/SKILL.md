---
name: role-prompting
description: Rewrite plain user requests into stronger task-specific role prompts before solving them.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [prompting, role-prompts, writing, web-development, analysis]
---

# Role Prompting Skill

Use this skill when the user gives a plain task request and you want to rewrite it into a stronger role-based prompt before solving it.

## Goal

Convert a direct user request into a task-specific role prompt that:
- frames the model as a strong domain expert
- preserves the user's original request
- adds a short, relevant quality bar
- keeps assumptions minimal and explicit

## Core rule

Do **not** replace the user's goal. Rewrite it into a better prompt wrapper while keeping the original ask intact.

## Workflow

1. Identify the likely task domain.
2. Pick a role that matches that domain.
3. Preserve the user's actual request in the rewritten prompt.
4. Add one short quality bar tailored to the domain.
5. If subject matter is obvious, mention it briefly.
6. Then solve the task using the rewritten prompt internally.

## Recommended prompt pattern

```text
You are [strong domain role]. You are also deeply familiar with [subject].
[Original request, preserved but cleaned up.]
[Short quality bar specific to the task.]
If important details are missing, make reasonable assumptions and state them briefly.
```

## Domain templates

### Web development
Use roles like:
- world-class web designer
- frontend developer
- UX strategist

Quality bar ideas:
- clean UX
- strong structure
- polished visual hierarchy
- accessibility

### Creative writing
Use roles like:
- world-class creative writer
- storyteller
- editor with strong voice and pacing instincts

Quality bar ideas:
- vivid imagery
- emotional resonance
- memorable voice
- tight prose

### Analysis
Use roles like:
- world-class analyst
- strategic thinker
- critical evaluator

Quality bar ideas:
- explicit assumptions
- decision-relevant insights
- rigor over fluff

### Marketing
Use roles like:
- world-class marketer
- copywriter
- brand strategist

Quality bar ideas:
- audience fit
- persuasion
- clarity
- conversion focus

### Software development
Use roles like:
- world-class software engineer
- product-minded developer
- careful code reviewer

Quality bar ideas:
- correctness
- maintainability
- clear architecture
- edge cases

## Example rewrites

User:
```text
build me a website about hot dogs
```

Internal rewrite:
```text
You are a world-class web designer and frontend developer with strong information architecture instincts. You are also deeply familiar with the subject matter for this task: hot dogs. Build me a website about hot dogs. Prioritize clean UX, strong structure, accessible copy, and polished visual hierarchy. If important details are missing, make reasonable assumptions and state them briefly.
```

User:
```text
write me a spooky bedtime story about a lighthouse
```

Internal rewrite:
```text
You are a world-class creative writer and storyteller with excellent command of tone, pacing, and imagery. You are also deeply familiar with the subject matter for this task: a lighthouse. Write me a spooky bedtime story about a lighthouse. Prioritize originality, emotional resonance, memorable voice, and tight prose. If important details are missing, make reasonable assumptions and state them briefly.
```

## Cautions

- This is a steering technique, not a guarantee of better factual accuracy.
- Do not let the role prompt create fake certainty.
- For factual, current, or technical claims, still verify with tools when needed.
- If the user's request already specifies a role or style, prefer the user's wording.
