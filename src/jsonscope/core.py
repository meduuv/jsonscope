import json
from typing import Any


def load_text(text: str) -> Any:
    return json.loads(text)


def validate(text: str) -> bool:
    try:
        json.loads(text)
    except json.JSONDecodeError:
        return False
    return True


def format_json(value: Any, indent: int = 2) -> str:
    return json.dumps(value, indent=indent, ensure_ascii=False, sort_keys=False)


def compact(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def get_path(value: Any, path: str) -> Any:
    current = value
    if not path:
        return current
    for part in path.split("."):
        if isinstance(current, dict):
            if part not in current:
                raise KeyError(part)
            current = current[part]
        elif isinstance(current, list) and part.isdigit():
            index = int(part)
            if index >= len(current):
                raise IndexError(index)
            current = current[index]
        else:
            raise KeyError(part)
    return current


def inspect(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return {"type": "object", "keys": len(value), "key_names": list(value)}
    if isinstance(value, list):
        return {"type": "array", "items": len(value)}
    if value is None:
        return {"type": "null"}
    return {"type": type(value).__name__}
