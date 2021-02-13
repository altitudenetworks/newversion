# NewVersion - Your version manager

[![PyPI - newversion](https://img.shields.io/pypi/v/newversion.svg?color=blue&label=newversion)](https://pypi.org/project/newversion)
[![Docs](https://img.shields.io/readthedocs/newversion.svg?color=blue&label=Builder%20docs)](https://newversion.readthedocs.io/)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/newversion.svg?color=blue)](https://pypi.org/project/newversion)
[![Coverage](https://img.shields.io/codecov/c/github/vemel/newversion)](https://codecov.io/gh/vemel/newversion)

- Follows [PEP 440](https://www.python.org/dev/peps/pep-0440/)
- Fully compatible with [packaging.Version](https://packaging.pypa.io/en/latest/version.html)
- Brings version bumping from [semver](https://pypi.org/project/semver/)
- Comes with a helpful CLI tool `newversion`
- Shines in CI

- [NewVersion - Your version manager](#newversion---your-version-manager)
  - [Installation](#installation)
  - [Usage](#usage)
    - [CLI](#cli)
    - [Python library](#python-library)
  - [Versioning](#versioning)
  - [Latest changes](#latest-changes)

## Installation

```bash
python -m pip install newversion
```

## Usage

### CLI

```bash
newversion            # 0.0.0
newversion bump major # 1.0.0

python setup.py --version  # 1.2.3
python setup.py --version | newversion bump  # 1.2.4
python setup.py --version | newversion get minor  # 2

echo "1.2.3rc1" | newversion bump micro   # 1.2.4
echo "1.2.3rc1" | newversion bump minor   # 1.3.0
echo "1.2.3rc1" | newversion bump major   # 2.0.0
echo "1.2.3rc1" | newversion bump pre     # 1.2.3rc2
echo "1.2.3rc1" | newversion bump rc      # 1.2.3rc2
echo "1.2.3rc1" | newversion bump alpha   # 1.2.4a1

echo "1.2.3rc1" | newversion set micro 5  # 1.2.5rc1
echo "1.2.3rc1" | newversion set minor 5  # 1.5.3rc1
echo "1.2.3rc1" | newversion set major 5  # 5.2.3rc1
echo "1.2.3rc1" | newversion set pre 5    # 1.2.3rc5
echo "1.2.3rc1" | newversion set rc 5     # 1.2.3rc5
echo "1.2.3rc1" | newversion set alpha 5  # 1.2.3a5

echo "1.2.3rc1" | newversion get micro    # 1
echo "1.2.3rc1" | newversion get minor    # 2
echo "1.2.3rc1" | newversion get major    # 3
echo "1.2.3rc1" | newversion get pre      # rc1
echo "1.2.3rc1" | newversion get rc       # 1
echo "1.2.3rc1" | newversion get alpha    # 0

echo "1.2.3rc1" | newversion stable       # error!
echo "1.2.3" | newversion stable          # 1.2.3
echo "1.2.3" | newversion stable && echo "Stable!" # Stable!

echo "1.2.3rc1" | newversion gt "1.2.3"   # error!
echo "1.2.3rc1" | newversion lte "1.2.3"  # "1.2.3rc1"
```

### Python library

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
