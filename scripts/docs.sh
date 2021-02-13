#!/usr/bin/env bash
set -e

ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

handsdown --external 'https://github.com/vemel/newversion/blob/main/' -n newversion newversion --exclude '*/build/*' --cleanup --panic
