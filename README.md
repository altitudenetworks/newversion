# NewVersion - SemVer helpers for PEP-440 versions

[![PyPI - newversion](https://img.shields.io/pypi/v/newversion.svg?color=blue&label=newversion)](https://pypi.org/project/newversion)
[![Docs](https://img.shields.io/readthedocs/newversion.svg?color=blue&label=Builder%20docs)](https://newversion.readthedocs.io/)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/newversion.svg?color=blue)](https://pypi.org/project/newversion)
[![Coverage](https://img.shields.io/codecov/c/github/vemel/newversion)](https://codecov.io/gh/vemel/newversion)

- Fully compatible with [packaging.Version](https://packaging.pypa.io/en/latest/version.html)
- [semver](https://pypi.org/project/semver/)-style version bumping
- Keeps `Version` immutable, as it should be

## Installation

```bash
python -m pip install newversion
```

## Usage

```python
from newversion import Version

version = Version("1.2.3")
next_version = version.bump_minor() # Version("1.3.0")

# bump version same way as SemVer
version.dumps() # "1.2.3"
version.bump_micro().dumps() # "1.2.4"
version.bump_minor().dumps() # "1.3.0"
version.bump_major().dumps() # "2.0.0"

# create and bump pre-releases
version.bump_prerelease().dumps() # "1.2.4rc1"
version.bump_prerelease(bump_release="minor").dumps() # "1.3.0rc1"
version.bump_prerelease("alpha").dumps() # "1.2.4a1"
Version("1.2.3b4").bump_prerelease().dumps() # "1.2.3b5"
version.bump_micro().replace(dev=1234).dumps() # "1.2.4.dev1234"

# and post-releases
version.bump_postrelease().dumps() # "1.2.3.post1"
Version("1.2.3.post3").bump_postrelease(2).dumps() # "1.2.3.post5"

# easily check if this is a pre- or dev release or a stable version
Version("1.2.3").is_stable # True
Version("1.2.3a6").is_stable # False
Version("1.2.3.post3").is_stable # True
Version("1.2.3.post3").get_stable().dumps() # "1.2.3"
```

## Versioning

`newversion` version follows [PEP 440](https://www.python.org/dev/peps/pep-0440/).

## Latest changes

Full changelog can be found in [Releases](https://github.com/vemel/newversion/releases).
