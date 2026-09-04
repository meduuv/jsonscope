# JSONScope

> Inspect, validate, format and query JSON from the terminal.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

JSONScope is a dependency-free command-line toolkit for working with JSON files and stdin input.

## Features

- Pretty-print JSON
- Validate files and stdin input
- Inspect object keys and array structure
- Select nested values with dotted paths
- Compact JSON output
- Stable JSON output for scripts
- Clear command-line errors
- Small Python API

## Usage

```bash
jsonscope format data.json
jsonscope validate data.json
jsonscope get data.json user.profile.name
jsonscope compact data.json
```

See the full CLI reference with:

```bash
jsonscope --help
```

## Workflow

```text
JSON file / stdin
       ↓
    parse
       ↓
 inspect / validate / query / format
       ↓
 terminal or script output
```

JSONScope does not require a runtime service and is designed to work well inside shell scripts and developer workflows.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
