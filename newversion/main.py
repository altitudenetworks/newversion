import argparse
import sys

from newversion.cli_parser import parse_args
from newversion.executor import Executor, ExecutorError


class CLIError(Exception):
    """
    Main CLI error
    """


def main_api(config: argparse.Namespace) -> str:
    """
    Main API entrypoint.
    """
    executor = Executor(config)
    try:
        return executor.execute()
    except ExecutorError as e:
        raise CLIError(e)


def main_cli() -> None:
    """
    Main entrypoint for CLI.
    """
    config = parse_args(sys.argv[1:])
    try:
        output = main_api(config)
    except CLIError as e:
        sys.stderr.write(f"ERROR {e}\n")
        sys.exit(1)

    sys.stdout.write(f"{output}\n")
