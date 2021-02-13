"""
CLI commands executor.
"""
import argparse

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

    def execute(self) -> Version:
        commands = {
            "bump": self.command_bump,
            "stable": self.command_stable,
            "is_stable": self.command_is_stable,
            "lt": self.command_lt,
            "lte": self.command_lte,
            "gt": self.command_gt,
            "gte": self.command_gte,
            "eq": self.command_eq,
        }
        command = self.config.command
        if command in commands:
            return commands[self.config.command]()

        return self.input

    def command_bump(self) -> Version:
        return {
            "micro": self.input.bump_micro,
            "major": self.input.bump_major,
            "minor": self.input.bump_minor,
            "pre": self.input.bump_prerelease,
            "post": self.input.bump_postrelease,
        }[self.config.release](self.config.increment)

    def command_stable(self) -> Version:
        return self.input.get_stable()

    def command_is_stable(self) -> Version:
        if not self.input.is_stable:
            raise ExecutorError(f"Version {self.input} is not stable")
        return self.input

    def command_lt(self) -> Version:
        if not (self.input < self.other):
            raise ExecutorError(f"Version {self.input} is not lesser than {self.other}")
        return self.input

    def command_lte(self) -> Version:
        if not (self.input <= self.other):
            raise ExecutorError(
                f"Version {self.input} is not lesser or equal to {self.other}"
            )
        return self.input

    def command_gt(self) -> Version:
        if not (self.input > self.other):
            raise ExecutorError(
                f"Version {self.input} is not greater than {self.other}"
            )
        return self.input

    def command_gte(self) -> Version:
        if not (self.input >= self.other):
            raise ExecutorError(
                f"Version {self.input} is not greater or equal to {self.other}"
            )
        return self.input

    def command_eq(self) -> Version:
        if not (self.input == self.other):
            raise ExecutorError(f"Version {self.input} is not equal to {self.other}")
        return self.input
