# Main

> Auto-generated documentation for [newversion.main](https://github.com/vemel/newversion/blob/master/newversion/main.py) module.

- [newversion](../README.md#newversion---semver-helpers-for-pep-440-versions) / [Modules](../MODULES.md#newversion-modules) / [Newversion](index.md#newversion) / Main
    - [CLIError](#clierror)
    - [main_api](#main_api)
    - [main_cli](#main_cli)

## CLIError

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L8)

```python
class CLIError(Exception):
```

Main CLI error

## main_api

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L14)

```python
def main_api(config: argparse.Namespace) -> str:
```

Main API entrypoint.

## main_cli

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L25)

```python
def main_cli() -> None:
```

Main entrypoint for CLI.
