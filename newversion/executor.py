"""
CLI commands executor.
"""
import argparse

from newversion.constants import VersionParts
from newversion.version import Version


class ExecutorError(Exception):
    """
    Main CLI commands executor error.
    """


class Executor:
    """
    CLI commands executor.
    """

    def __init__(self, config: argparse.Namespace) -> None:
        self.config = config

    @property
    def input(self) -> Version:
        return self.config.input

    @property
    def other(self) -> Version:
        return self.config.other

    def execute(self) -> str:
        """
        Execute command based on `config`.

        Returns:
            Processed `Version`.
        """
        commands = dict(
            bump=self._command_bump,
            set=self._command_set,
            stable=self._command_stable,
            is_stable=self._command_is_stable,
            lt=self._command_lt,
            lte=self._command_lte,
            gt=self._command_gt,
            gte=self._command_gte,
            eq=self._command_eq,
        )
        command = self.config.command
        if command in commands:
            return commands[self.config.command]().dumps()

        if command == "get":
            return self._command_get()

        return self.input.dumps()

    def _command_get(self) -> str:
        release = self.config.release
        if release == VersionParts.LOCAL:
            return self.input.local[0] if self.input.local else ""

        if release == VersionParts.PRE:
            return f"{self.input.pre[0]}{self.input.pre[1]}" if self.input.pre else ""

        if release == VersionParts.POST:
            return str(self.input.post[-1]) if self.input.post else "0"

        if release == VersionParts.ALPHA:
            return str(self.input.pre[-1]) if self.input.pre and self.input.pre[0] == "a" else "0"

        if release == VersionParts.BETA:
            return str(self.input.pre[-1]) if self.input.pre and self.input.pre[0] == "b" else "0"

        if release == VersionParts.RC:
            return str(self.input.pre[-1]) if self.input.pre and self.input.pre[0] == "rc" else "0"

        if release == VersionParts.EPOCH:
            return str(self.input.epoch) if self.input.epoch else "0"

        result = dict(
            major=self.input.major,
            minor=self.input.minor,
            micro=self.input.micro,
        )[release]
        return str(result)

    def _command_bump(self) -> Version:
        if self.config.release in (
            VersionParts.MICRO,
            VersionParts.MAJOR,
            VersionParts.MINOR,
        ):
            return self.input.bump_release(self.config.release, self.config.increment)

        if self.config.release == VersionParts.PRE:
            return self.input.bump_prerelease(self.config.increment)

        if self.config.release == VersionParts.POST:
            return self.input.bump_postrelease(self.config.increment)

        if self.config.release in (
            VersionParts.RC,
            VersionParts.ALPHA,
            VersionParts.BETA,
        ):
            return self.input.bump_prerelease(self.config.increment, self.config.release)

        return self.input

    def _command_set(self) -> Version:
        value = self.config.value
        if self.config.release == VersionParts.PRE:
            if self.input.prerelease_type == VersionParts.ALPHA:
                return self.input.replace(alpha=value)
            if self.input.prerelease_type == VersionParts.BETA:
                return self.input.replace(beta=value)
            if self.input.prerelease_type == VersionParts.RC:
                return self.input.replace(rc=value)

            return self.input.replace(rc=value)

        kwargs = {self.config.release: value}
        return self.input.replace(**kwargs)

    def _command_stable(self) -> Version:
        return self.input.get_stable()

    def _command_is_stable(self) -> Version:
        if not self.input.is_stable:
            raise ExecutorError(f"Version {self.input} is not stable")
        return self.input

    def _command_lt(self) -> Version:
        if not (self.input < self.other):
            raise ExecutorError(f"Version {self.input} is not lesser than {self.other}")
        return self.input

    def _command_lte(self) -> Version:
        if not (self.input <= self.other):
            raise ExecutorError(f"Version {self.input} is not lesser or equal to {self.other}")
        return self.input

    def _command_gt(self) -> Version:
        if not (self.input > self.other):
            raise ExecutorError(f"Version {self.input} is not greater than {self.other}")
        return self.input

    def _command_gte(self) -> Version:
        if not (self.input >= self.other):
            raise ExecutorError(f"Version {self.input} is not greater or equal to {self.other}")
        return self.input

    def _command_eq(self) -> Version:
        if not (self.input == self.other):
            raise ExecutorError(f"Version {self.input} is not equal to {self.other}")
        return self.input
