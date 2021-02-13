# Cli Parser

> Auto-generated documentation for [newversion.cli_parser](https://github.com/vemel/newversion/blob/main/newversion/cli_parser.py) module.

Main CLI parser.

- [newversion](../README.md#newversion---your-version-manager) / [Modules](../MODULES.md#newversion-modules) / [Newversion](index.md#newversion) / Cli Parser
    - [get_stdin](#get_stdin)
    - [parse_args](#parse_args)

## get_stdin

[[find in source code]](https://github.com/vemel/newversion/blob/main/newversion/cli_parser.py#L14)

```python
def get_stdin() -> Version:
```

Get input from stdin.

#### Returns

Parsed version.

#### See also

- [Version](version.md#version)

## parse_args

[[find in source code]](https://github.com/vemel/newversion/blob/main/newversion/cli_parser.py#L30)

```python
def parse_args(args: Sequence[str]) -> argparse.Namespace:
```

Main CLI parser.

#### Returns

Argument parser Namespace.
