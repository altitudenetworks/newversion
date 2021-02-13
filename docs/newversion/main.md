# Main

> Auto-generated documentation for [newversion.main](https://github.com/vemel/newversion/blob/master/newversion/main.py) module.

Extended `packaging.version.Version` implementation.

- [newversion](../README.md#newversion) / [Modules](../MODULES.md#newversion-modules) / [Newversion](index.md#newversion) / Main
    - [Version](#version)
        - [Version().base](#versionbase)
        - [Version().base](#versionbase)
        - [Version().bump_major](#versionbump_major)
        - [Version().bump_micro](#versionbump_micro)
        - [Version().bump_minor](#versionbump_minor)
        - [Version().bump_postrelease](#versionbump_postrelease)
        - [Version().bump_prerelease](#versionbump_prerelease)
        - [Version().copy](#versioncopy)
        - [Version().dumps](#versiondumps)
        - [Version().get_devrelease](#versionget_devrelease)
        - [Version().get_stable](#versionget_stable)
        - [Version().is_stable](#versionis_stable)
        - [Version.zero](#versionzero)
    - [VersionError](#versionerror)

## Version

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L17)

```python
class Version(PkgVersion):
    def __init__(version: str) -> None:
```

Extended `packaging.version.Version` implementation.

### Version().base

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L41)

```python
@property
def base() -> BaseVersion:
```

Underlying version NamedTuple.

### Version().base

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L48)

```python
@base.setter
def base(base: BaseVersion) -> None:
```

### Version().bump_major

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L63)

```python
def bump_major(inc: int = 1) -> _R:
```

Get next major version.

#### Arguments

- `inc` - Increment for major version.

#### Examples

```python
Version("1.2.3").bump_major()  # "2.0.0"
Version("1.2.3.dev14").bump_major()  # "2.0.0"
Version("1.2.3a5").bump_major()  # "2.0.0"
Version("1.2.3rc3").bump_major(2)  # "3.0.0"
Version("1.2.3rc3").bump_major(0)  # "1.0.0"
```

#### Returns

A new copy.

### Version().bump_micro

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L125)

```python
def bump_micro(inc: int = 1) -> _R:
```

Get next micro version.

#### Arguments

- `inc` - Increment for micro version.

#### Examples

```python
Version("1.2.3").bump_micro()  # "1.2.4"
Version("1.2.3.dev14").bump_micro()  # "1.2.4"
Version("1.2.3a5").bump_micro()  # "1.2.4"
Version("1.2.3rc3").bump_micro(2)  # "1.2.5"
Version("1.2.3rc3").bump_micro(0)  # "1.2.3"
```

#### Returns

A new copy.

### Version().bump_minor

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L94)

```python
def bump_minor(inc: int = 1) -> _R:
```

Get next minor version.

#### Arguments

- `inc` - Increment for minor version.

#### Examples

```python
Version("1.2.3").bump_minor()  # "1.3.0"
Version("1.2.3.dev14").bump_minor()  # "1.3.0"
Version("1.2.3a5").bump_minor()  # "1.3.0"
Version("1.2.3rc3").bump_minor(2)  # "1.4.0"
Version("1.2.3rc3").bump_minor(0)  # "1.2.0"
```

#### Returns

A new copy.

### Version().bump_postrelease

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L191)

```python
def bump_postrelease(inc: int = 1) -> _R:
```

Get next postrelease version.

#### Arguments

- `inc` - Increment for micro version.

#### Examples

```python
Version("1.2.3").bump_postrelease()  # "1.2.3.post1"
Version("1.2.3.post3").bump_postrelease()  # "1.2.3.post4"
Version("1.2.3a5").bump_postrelease()  # "1.2.3.post1"
Version("1.2.3.post4").bump_postrelease(2)  # "1.2.3.post6"
```

#### Returns

A new copy.

### Version().bump_prerelease

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L156)

```python
def bump_prerelease(inc: int = 1, default_letter: str = 'rc') -> _R:
```

Get next prerelease version.

#### Arguments

- `inc` - Increment for micro version.
- `default_letter` - Prerelease letter if version is not a prerelease.

#### Examples

```python
Version("1.2.3").bump_prerelease()  # "1.2.3.rc1"
Version("1.2.3.dev14").bump_prerelease()  # "1.2.3.rc1"
Version("1.2.3a5").bump_prerelease()  # "1.2.3a6"
Version("1.2.3rc3").bump_prerelease(2, "beta")  # "1.2.3rc5"
```

#### Returns

A new copy.

### Version().copy

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L52)

```python
def copy() -> _R:
```

Create a copy of a current version instance.

### Version().dumps

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L35)

```python
def dumps() -> str:
```

Render to string.

### Version().get_devrelease

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L224)

```python
def get_devrelease(number: int) -> _R:
```

Get prerelease version from next version with `dev` postfix.

#### Examples

```python
Version("1.2.3").get_dev_prerelease(24) # "1.2.4.dev24"
Version("1.2.3rc5").get_dev_prerelease(17) # "1.2.4.dev17"
Version("1.2.3.dev20").get_dev_prerelease(21) # "1.2.3.dev21"
Version("1.2.3.post4").get_dev_prerelease(21) # "1.2.4.dev21"
```

#### Arguments

- `number` - Dev prerelease number.

#### Returns

A new instance.

### Version().get_stable

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L267)

```python
def get_stable() -> _R:
```

Get stable version from pre- or post- release.

#### Examples

```python
Version("1.2.3").get_stable() # "1.2.3"
Version("2.1.0a2").get_stable() # "2.1.0"
Version("1.2.5.post3").get_stable() # "1.2.5"
```

#### Returns

A new instance.

### Version().is_stable

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L257)

```python
@property
def is_stable() -> bool:
```

Whether version is not prerelease or devrelease.

#### Returns

True if it is stable.

### Version.zero

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L28)

```python
@classmethod
def zero() -> _R:
```

Get zero version `0.0.0`

## VersionError

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/main.py#L13)

```python
class VersionError(InvalidVersion):
```
