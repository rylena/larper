from role_prompt_skill.transformer import classify_task, transform_prompt


def test_classifies_web_dev_prompt():
    result = classify_task("build me a website about hot dogs")
    assert result.domain == "web_development"
    assert "web designer" in result.role


def test_transforms_web_dev_prompt_with_original_request_preserved():
    prompt = transform_prompt("build me a website about hot dogs")
    assert prompt.startswith("You are")
    assert "world-class web designer" in prompt
    assert "hot dogs" in prompt
    assert "Build me a website about hot dogs." in prompt


def test_classifies_creative_writing_prompt():
    result = classify_task("write me a spooky bedtime story about a lighthouse")
    assert result.domain == "creative_writing"
    assert "creative writer" in result.role


def test_transforms_creative_writing_prompt_with_style_guidance():
    prompt = transform_prompt("write me a spooky bedtime story about a lighthouse")
    assert "storyteller" in prompt
    assert "spooky bedtime story about a lighthouse" in prompt
    assert "voice" in prompt


def test_classifies_analysis_prompt():
    result = classify_task("analyze this startup idea and tell me if it has product-market fit")
    assert result.domain == "analysis"
    assert "analyst" in result.role


def test_classifies_marketing_prompt():
    result = classify_task("write ad copy for a new matcha energy drink")
    assert result.domain == "marketing"
    assert "marketer" in result.role


def test_falls_back_to_generalist_for_unknown_prompt():
    result = classify_task("help me think through this weird problem")
    assert result.domain == "general"
    assert "generalist" in result.role


def test_json_ready_metadata_shape():
    result = classify_task("build a landing page for a robotics startup")
    payload = result.to_dict()
    assert set(payload) == {"domain", "role", "subject", "quality_bar"}
    assert payload["subject"] == "a robotics startup"
