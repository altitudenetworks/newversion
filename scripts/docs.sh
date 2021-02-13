#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

handsdown --external `git config --get remote.origin.url` -n newversion newversion --exclude '*/build/*' --cleanup --panic
