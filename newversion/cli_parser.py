"""
Main CLI parser.
"""
import argparse
import sys
from typing import Sequence

import pkg_resources

from newversion.constants import VersionParts
from newversion.version import Version


def get_stdin() -> Version:
    """
    Get input from stdin.

    Returns:
        Parsed version.
    """
    if sys.stdin.isatty():
        return Version.zero()

    for line in sys.stdin.readlines():
        return Version(line.strip().split(" ")[-1])

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
    parser.add_argument("-V", "--version", action="version", version=version, help="Show version")
    parser.add_argument(
        "-i",
        "--input",
        type=Version,
        default=None,
        help="Input version, can be provided as a pipe-in as well.",
    )
    subparsers = parser.add_subparsers(help="Available subcommands", dest="command")
    parser_bump = subparsers.add_parser("bump", help="Bump current version")
    parser_bump.add_argument(
        "release",
        choices=[
            VersionParts.MAJOR,
            VersionParts.MINOR,
            VersionParts.MICRO,
            VersionParts.PRE,
            VersionParts.POST,
            VersionParts.RC,
            VersionParts.ALPHA,
            VersionParts.BETA,
        ],
        nargs="?",
        default="micro",
        help="Release type. Default: micro",
    )
    parser_bump.add_argument(
        "increment",
        type=int,
        default=1,
        nargs="?",
        help="Version increment. Default: 1",
    )

    parser_get = subparsers.add_parser("get", help="Get release number")
    parser_get.add_argument(
        "release",
        choices=[
            VersionParts.MAJOR,
            VersionParts.MINOR,
            VersionParts.MICRO,
            VersionParts.PRE,
            VersionParts.POST,
            VersionParts.DEV,
            VersionParts.RC,
            VersionParts.ALPHA,
            VersionParts.BETA,
            VersionParts.EPOCH,
            VersionParts.LOCAL,
        ],
        help="Release type",
    )

    parser_set = subparsers.add_parser("set", help="Set release number")
    parser_set.add_argument(
        "release",
        choices=[
            VersionParts.MAJOR,
            VersionParts.MINOR,
            VersionParts.MICRO,
            VersionParts.PRE,
            VersionParts.POST,
            VersionParts.DEV,
            VersionParts.RC,
            VersionParts.ALPHA,
            VersionParts.BETA,
            VersionParts.EPOCH,
        ],
        help="Release type",
    )
    parser_set.add_argument(
        "value",
        type=int,
        help="Release number",
    )

    subparsers.add_parser("stable", help="Get stable release of current version")
    subparsers.add_parser(
        "is_stable",
        help="Check if current version is not a pre- or dev release",
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

    result = parser.parse_args(args)

    if result.input is None:
        result.input = get_stdin()

    return result
