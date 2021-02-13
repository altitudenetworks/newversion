# Version

> Auto-generated documentation for [newversion.version](https://github.com/vemel/newversion/blob/master/newversion/version.py) module.

Extended `packaging.version.Version` implementation.

- [newversion](../README.md#newversion---semver-helpers-for-pep-440-versions) / [Modules](../MODULES.md#newversion-modules) / [Newversion](index.md#newversion) / Version
    - [Version](#version)
        - [Version().base](#versionbase)
        - [Version().base](#versionbase)
        - [Version().bump_major](#versionbump_major)
        - [Version().bump_micro](#versionbump_micro)
        - [Version().bump_minor](#versionbump_minor)
        - [Version().bump_postrelease](#versionbump_postrelease)
        - [Version().bump_prerelease](#versionbump_prerelease)
        - [Version().bump_release](#versionbump_release)
        - [Version().copy](#versioncopy)
        - [Version().dumps](#versiondumps)
        - [Version().get_major](#versionget_major)
        - [Version().get_stable](#versionget_stable)
        - [Version().is_stable](#versionis_stable)
        - [Version().prerelease_type](#versionprerelease_type)
        - [Version().replace](#versionreplace)
        - [Version.zero](#versionzero)
    - [VersionError](#versionerror)

## Version

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L20)

```python
class Version(PkgVersion):
    def __init__(version: str) -> None:
```

Extended `packaging.version.Version` implementation.

### Version().base

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L59)

```python
@property
def base() -> BaseVersion:
```

Underlying version NamedTuple.

### Version().base

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L66)

```python
@base.setter
def base(base: BaseVersion) -> None:
```

### Version().bump_major

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L111)

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

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L173)

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

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L142)

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

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L255)

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

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L204)

```python
def bump_prerelease(
    inc: int = 1,
    release_type: Literal['rc', 'alpha', 'beta', 'a', 'b'] = None,
    bump_release: Literal['major', 'minor', 'micro'] = VersionParts.MICRO,
) -> _R:
```

Get next prerelease version.
If version is stable - bump `micro` for a proper versioning as well.
Defaults to `rc` pre-releases.

#### Arguments

- `inc` - Increment for micro version.
- `release_type` - Prerelease type: alpha, beta, rc.
- `bump_release` - Release number to bump if version is stable.

#### Examples

```python
Version("1.2.3").bump_prerelease()  # "1.2.4rc1"
Version("1.2.3").bump_prerelease(bump_release="major")  # "2.0.0rc1"
Version("1.2.3.dev14").bump_prerelease()  # "1.2.3rc1"
Version("1.2.3a5").bump_prerelease()  # "1.2.3a6"
Version("1.2.3rc3").bump_prerelease(2, "beta")  # "1.2.3rc5"
```

#### Returns

A new copy.

### Version().bump_release

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L81)

```python
def bump_release(
    release_type: Literal['major', 'minor', 'micro'] = VersionParts.MICRO,
    inc: int = 1,
) -> _R:
```

Get next release version.

#### Arguments

- `release_type` - Release type: major, minor, micro.
- `inc` - Increment for major version.

#### Examples

```python
Version("1.2.3").bump_release()  # "1.2.4"
Version("1.2.3").bump_release("major")  # "2.0.0"
Version("1.2.3.dev14").bump_release("minor", 2)  # "1.4.0"
```

#### Returns

A new copy.

### Version().copy

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L70)

```python
def copy() -> _R:
```

Create a copy of a current version instance.

### Version().dumps

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L38)

```python
def dumps() -> str:
```

Render to string.

### Version().get_major

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L389)

```python
def get_major(number: int) -> _R:
```

### Version().get_stable

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L360)

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

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L350)

```python
@property
def is_stable() -> bool:
```

Whether version is not prerelease or devrelease.

#### Returns

True if it is stable.

### Version().prerelease_type

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L44)

```python
@property
def prerelease_type() -> Optional[Literal['rc', 'alpha', 'beta']]:
```

### Version().replace

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L288)

```python
def replace(
    major: Optional[int] = None,
    minor: Optional[int] = None,
    micro: Optional[int] = None,
    alpha: Optional[int] = None,
    beta: Optional[int] = None,
    rc: Optional[int] = None,
    dev: Optional[int] = None,
    post: Optional[int] = None,
    epoch: Optional[int] = None,
    local: Optional[str] = None,
) -> _R:
```

Modify version parts.

#### Examples

```python
Version("1.2.3").replace(dev=24) # "1.2.3.dev24"
Version("1.2.3rc5").replace(17) # "1.2.3.dev17"
```

#### Arguments

- `major` - Major release number.
- `minor` - Minor release number.
- `micro` - Micro release number.
- `alpha` - Alpha pre-release number.
- `beta` - Beta pre-release number.
- `rc` - RC pre-release number.
- `dev` - Dev release number.
- `post` - Post release number.
- `epoch` - Release epoch.
- `local` - Local release identifier.

#### Returns

A new instance.

### Version.zero

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L31)

```python
@classmethod
def zero() -> _R:
```

Get zero version `0.0.0`

## VersionError

[[find in source code]](https://github.com/vemel/newversion/blob/master/newversion/version.py#L16)

```python
class VersionError(InvalidVersion):
```
