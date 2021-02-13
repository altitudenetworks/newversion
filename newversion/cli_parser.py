"""
Main CLI parser.
"""
import argparse
import select
import sys
from typing import Sequence

import pkg_resources

from newversion.version import Version


def get_stdin() -> Version:
    if select.select([sys.stdin], [], [], 0.0)[0]:
        for line in sys.stdin:
            return Version(line.split(" ")[-1].strip())

    return Version.zero()


def parse_args(args: Sequence[str]) -> argparse.Namespace:
    """
    Main CLI parser.

    Returns:
        Argument parser Namespace.
    """
    try:
        version = pkg_resources.get_distribution("newversion").version
    except pkg_resources.DistributionNotFound:
        version = "0.0.0"

    parser = argparse.ArgumentParser(
        "newversion",
        description="SemVer helpers for PEP-440 versions",
    )
    parser.add_argument(
        "-V", "--version", action="version", version=version, help="Show version"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Version,
        default=get_stdin(),
        help="Input version, can be provided as a pipe-in as well.",
    )
    subparsers = parser.add_subparsers(help="Available subcommands", dest="command")
    parser_bump = subparsers.add_parser("bump", help="Bump current version")
    parser_bump.add_argument(
        "release",
        choices=["major", "minor", "micro", "pre", "post"],
        nargs="?",
        default="micro",
        help="Release type. Default: micro",
    )
    parser_bump.add_argument(
        "increment",
        type=int,
        default=1,
        nargs="?",
        help="Increment. Default: 1",
    )

    subparsers.add_parser("stable", help="Get stable release of current version")
    subparsers.add_parser(
        "is_stable",
        help="Raise error if current version is a pre- or dev release",
    )
    parser_lt = subparsers.add_parser(
        "lt",
        help="Check if current version is lesser than the other",
    )
    parser_lt.add_argument(
        "other",
        type=Version,
        help="Version to compare",
    )

    parser_lte = subparsers.add_parser(
        "lte",
        help="Check if current version is lesser or equal to the other",
    )
    parser_lte.add_argument(
        "other",
        type=Version,
        help="Version to compare",
    )

    parser_gt = subparsers.add_parser(
        "gt",
        help="Check if current version is greater than the other",
    )
    parser_gt.add_argument(
        "other",
        type=Version,
        help="Version to compare",
    )

    parser_gte = subparsers.add_parser(
        "gte",
        help="Check if current version is greater or equal to the other",
    )
    parser_gte.add_argument(
        "other",
        type=Version,
        help="Version to compare",
    )

    parser_eq = subparsers.add_parser(
        "eq",
        help="Check if current version is equal to the other",
    )
    parser_eq.add_argument(
        "other",
        type=Version,
        help="Version to compare",
    )

    return parser.parse_args(args)
