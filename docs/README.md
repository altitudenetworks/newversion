# newversion

> Auto-generated documentation index.

Version manager compatible with packaging

Full newversion project documentation can be found in [Modules](MODULES.md#newversion-modules)

- [newversion](#newversion)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Versioning](#versioning)
    - [Latest changes](#latest-changes)
  - [newversion Modules](MODULES.md#newversion-modules)

## Installation

```bash
python -m pip install newversion
```

## Usage

```
from newversion import Version

version = Version("1.2.3")

# bump version same way as SemVer
version.dumps() # "1.2.3"
version.bump_micro().dumps() # "1.2.4"
version.bump_minor().dumps() # "1.3.0"
version.bump_major().dumps() # "2.0.0"

# create and bump pre-releases
version.bump_minor().bump_prerelease().dumps() # "1.3.0rc1"
version.bump_prerelease("alpha").dumps() # "1.2.3a1"
Version("1.2.3b4").bump_prerelease().dumps() # "1.2.3b5"
version.get_devrelease(1234).dumps() # "1.2.3.dev1234"

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
