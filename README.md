# JSONScope

A dependency-free command-line toolkit for inspecting, validating, formatting, and querying JSON data.

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

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

Built by Medu: https://guns.lol/meduu
