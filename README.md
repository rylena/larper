# Larper

Turn plain user requests into stronger, task-specific role prompts.

This repo contains:
- a reusable Hermes skill (`skill/role-prompting/SKILL.md`)
- a small Python library and CLI for prompt transformation
- tests covering web development, creative writing, analysis, and marketing cases

## What it does

Instead of treating a request like:

> build me a website about hot dogs

it rewrites it into a prompt more like:

> You are a world-class web designer and frontend developer with strong information architecture instincts. You are also deeply familiar with the subject matter for this task: hot dogs. Build me a website about hot dogs. Prioritize clean UX, strong structure, accessible copy, and polished visual hierarchy. If important details are missing, make reasonable assumptions and state them briefly. Keep the response directly useful for the original request.

The goal is not to make the model magically smarter. The goal is to give the model a better starting frame for the task.

## Project layout

- `skill/role-prompting/SKILL.md` — Hermes skill definition
- `src/larper/transformer.py` — prompt transformation logic
- `src/larper/cli.py` — command-line interface
- `tests/test_transformer.py` — automated tests
- `examples/prompts.md` — example prompt conversions

## Install

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```

## Usage

### Python

```python
from larper.transformer import transform_prompt

print(transform_prompt("build me a website about hot dogs"))
```

### CLI

```bash
python -m larper.cli "build me a website about hot dogs"
```

Or JSON output:

```bash
python -m larper.cli --json "write me a spooky bedtime story about a lighthouse"
```

## Test

```bash
pytest -q
```

## Design notes

The transformer uses lightweight heuristics:
- detect the likely task domain from the request
- select a role prompt template for that domain
- preserve the original user ask in the rewritten prompt
- add a short quality bar tailored to the task
- ask the model to make reasonable assumptions when details are missing

This keeps the behavior transparent and easy to adjust.
