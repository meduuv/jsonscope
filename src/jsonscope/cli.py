import argparse
import json
import sys
from pathlib import Path

from .core import compact, format_json, get_path, inspect


def read_input(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(prog="jsonscope")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("format", "compact", "validate", "inspect"):
        sub.add_parser(name).add_argument("file")
    get_parser = sub.add_parser("get")
    get_parser.add_argument("file")
    get_parser.add_argument("path")
    args = parser.parse_args()

    try:
        raw = read_input(args.file)
        value = json.loads(raw)
        if args.command == "format":
            print(format_json(value))
        elif args.command == "compact":
            print(compact(value))
        elif args.command == "validate":
            print("valid")
        elif args.command == "inspect":
            print(format_json(inspect(value)))
        else:
            print(format_json(get_path(value, args.path)))
    except (OSError, json.JSONDecodeError, KeyError, IndexError) as exc:
        print(f"jsonscope: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
