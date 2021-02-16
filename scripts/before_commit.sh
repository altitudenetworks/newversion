#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

npx pyright
pytest
black .
isort .
flake8 newversion

./scripts/docs.sh
