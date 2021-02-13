"""
Extended `packaging.version.Version` implementation.
"""
from typing import Optional, Tuple, Type, TypeVar

from packaging.version import InvalidVersion
from packaging.version import Version as PkgVersion
from packaging.version import _Version as BaseVersion  # type: ignore

_R = TypeVar("_R", bound="Version")


class VersionError(InvalidVersion):
    pass


class Version(PkgVersion):
    """
    Extended `packaging.version.Version` implementation.
    """

    def __init__(self, version: str) -> None:
        try:
            super().__init__(version)
        except InvalidVersion as e:
            raise VersionError(e)

    @classmethod
    def zero(cls: Type[_R]) -> _R:
        """
        Get zero version `0.0.0`
        """
        return cls("0.0.0")

    def dumps(self) -> str:
        """
        Render to string.
        """
        return str(self)

    @property
    def base(self) -> BaseVersion:
        """
        Underlying version NamedTuple.
        """
        return self._version

    @base.setter
    def base(self, base: BaseVersion) -> None:
        self._version = base

    def copy(self: _R) -> _R:
        """
        Create a copy of a current version instance.
        """
        return self.__class__(self.dumps())

    def _replace(self: _R, base: BaseVersion) -> _R:
        new_version = self.copy()
        new_version.base = base
        return new_version.copy()

    def bump_major(self: _R, inc: int = 1) -> _R:
        """
        Get next major version.

        Arguments:
            inc -- Increment for major version.

        Examples:

            ```python
            Version("1.2.3").bump_major()  # "2.0.0"
            Version("1.2.3.dev14").bump_major()  # "2.0.0"
            Version("1.2.3a5").bump_major()  # "2.0.0"
            Version("1.2.3rc3").bump_major(2)  # "3.0.0"
            Version("1.2.3rc3").bump_major(0)  # "1.0.0"
            ```

        Returns:
            A new copy.
        """
        return self._replace(
            BaseVersion(
                epoch=0,
                release=(self.major + inc, 0, 0),
                pre=None,
                post=None,
                dev=None,
                local=None,
            )
        )

    def bump_minor(self: _R, inc: int = 1) -> _R:
        """
        Get next minor version.

        Arguments:
            inc -- Increment for minor version.

        Examples:

            ```python
            Version("1.2.3").bump_minor()  # "1.3.0"
            Version("1.2.3.dev14").bump_minor()  # "1.3.0"
            Version("1.2.3a5").bump_minor()  # "1.3.0"
            Version("1.2.3rc3").bump_minor(2)  # "1.4.0"
            Version("1.2.3rc3").bump_minor(0)  # "1.2.0"
            ```

        Returns:
            A new copy.
        """
        return self._replace(
            BaseVersion(
                epoch=0,
                release=(self.major, self.minor + inc, 0),
                pre=None,
                post=None,
                dev=None,
                local=None,
            )
        )

    def bump_micro(self: _R, inc: int = 1) -> _R:
        """
        Get next micro version.

        Arguments:
            inc -- Increment for micro version.

        Examples:

            ```python
            Version("1.2.3").bump_micro()  # "1.2.4"
            Version("1.2.3.dev14").bump_micro()  # "1.2.4"
            Version("1.2.3a5").bump_micro()  # "1.2.4"
            Version("1.2.3rc3").bump_micro(2)  # "1.2.5"
            Version("1.2.3rc3").bump_micro(0)  # "1.2.3"
            ```

        Returns:
            A new copy.
        """
        return self._replace(
            BaseVersion(
                epoch=0,
                release=(self.major, self.minor, self.micro + inc),
                pre=None,
                post=None,
                dev=None,
                local=None,
            )
        )

    def bump_prerelease(self: _R, inc: int = 1, default_letter: str = "rc") -> _R:
        """
        Get next prerelease version.

        Arguments:
            inc -- Increment for micro version.
            default_letter -- Prerelease letter if version is not a prerelease.

        Examples:

            ```python
            Version("1.2.3").bump_prerelease()  # "1.2.3.rc1"
            Version("1.2.3.dev14").bump_prerelease()  # "1.2.3.rc1"
            Version("1.2.3a5").bump_prerelease()  # "1.2.3a6"
            Version("1.2.3rc3").bump_prerelease(2, "beta")  # "1.2.3rc5"
            ```

        Returns:
            A new copy.
        """
        pre = (default_letter, max(inc, 1))
        base_pre: Optional[Tuple[str, int]] = self._version.pre  # type: ignore
        if base_pre:
            pre = (base_pre[0], max(base_pre[1], 1) + inc)

        base = BaseVersion(
            epoch=0,
            release=self._version.release,  # type: ignore
            pre=pre,
            post=None,
            dev=None,
            local=None,
        )
        return self._replace(base)

    def bump_postrelease(self: _R, inc: int = 1) -> _R:
        """
        Get next postrelease version.

        Arguments:
            inc -- Increment for micro version.

        Examples:

            ```python
            Version("1.2.3").bump_postrelease()  # "1.2.3.post1"
            Version("1.2.3.post3").bump_postrelease()  # "1.2.3.post4"
            Version("1.2.3a5").bump_postrelease()  # "1.2.3.post1"
            Version("1.2.3.post4").bump_postrelease(2)  # "1.2.3.post6"
            ```

        Returns:
            A new copy.
        """
        post = ("post", max(inc, 1))
        base_post: Optional[Tuple[str, int]] = self._version.post  # type: ignore
        if base_post:
            post = ("post", max(base_post[1], 1) + inc)
        base = BaseVersion(
            epoch=0,
            release=self._version.release,  # type: ignore
            pre=None,
            post=post,
            dev=None,
            local=None,
        )
        return self._replace(base)

    def get_devrelease(self: _R, number: int) -> _R:
        """
        Get prerelease version from next version with `dev` postfix.

        Examples:

            ```python
            Version("1.2.3").get_dev_prerelease(24) # "1.2.4.dev24"
            Version("1.2.3rc5").get_dev_prerelease(17) # "1.2.4.dev17"
            Version("1.2.3.dev20").get_dev_prerelease(21) # "1.2.3.dev21"
            Version("1.2.3.post4").get_dev_prerelease(21) # "1.2.4.dev21"
            ```

        Arguments:
            number -- Dev prerelease number.

        Returns:
            A new instance.
        """
        next_version = self.bump_micro()
        if self.is_devrelease:
            next_version = self.copy()

        base = BaseVersion(
            epoch=next_version.base.epoch,  # type: ignore
            release=next_version.base.release,  # type: ignore
            pre=next_version.base.pre,  # type: ignore
            post=next_version.base.post,  # type: ignore
            dev=("dev", number),
            local=next_version.base.local,  # type: ignore
        )
        return self._replace(base)

    @property
    def is_stable(self) -> bool:
        """
        Whether version is not prerelease or devrelease.

        Returns:
            True if it is stable.
        """
        return not self.is_prerelease

    def get_stable(self: _R) -> _R:
        """
        Get stable version from pre- or post- release.

        Examples:

            ```python
            Version("1.2.3").get_stable() # "1.2.3"
            Version("2.1.0a2").get_stable() # "2.1.0"
            Version("1.2.5.post3").get_stable() # "1.2.5"
            ```

        Returns:
            A new instance.
        """
        return self.bump_micro(0)
