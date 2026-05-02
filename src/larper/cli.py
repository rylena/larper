from __future__ import annotations

import argparse
import json

from .transformer import classify_task, transform_prompt


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Turn a plain request into a role prompt.")
    parser.add_argument("request", help="The original user request to transform")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Return metadata and transformed prompt as JSON")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    profile = classify_task(args.request)
    prompt = transform_prompt(args.request)

    if args.as_json:
        payload = profile.to_dict()
        payload["prompt"] = prompt
        print(json.dumps(payload, indent=2))
        return

    print(prompt)


if __name__ == "__main__":
    main()
