# Executor

> Auto-generated documentation for [newversion.executor](https://github.com/vemel/newversion/blob/master/newversion/executor.py) module.

CLI commands executor.

- [newversion](../README.md#newversion---your-version-manager) / [Modules](../MODULES.md#newversion-modules) / [Newversion](index.md#newversion) / Executor
    - [Executor](#executor)
        - [Executor().execute](#executorexecute)
        - [Executor().input](#executorinput)
        - [Executor().other](#executorother)
    - [ExecutorError](#executorerror)

## Executor

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/executor.py#L16)

```python
class Executor():
    def __init__(config: argparse.Namespace) -> None:
```

CLI commands executor.

### Executor().execute

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/executor.py#L32)

```python
def execute() -> str:
```

Execute command based on `config`.

#### Returns

Processed `Version`.

### Executor().input

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/executor.py#L24)

```python
@property
def input() -> Version:
```

#### See also

- [Version](version.md#version)

### Executor().other

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/executor.py#L28)

```python
@property
def other() -> Version:
```

#### See also

- [Version](version.md#version)

## ExecutorError

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/executor.py#L10)

```python
class ExecutorError(Exception):
```

Main CLI commands executor error.
