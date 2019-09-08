#!/usr/bin/env bash

script_path="$( cd "$(dirname "$0")" ; pwd -P )"
install() {
echo start installing
cat  << EOF > .envrc
pyenv install 3.7.3 --skip-existing
if [ ! -e .venv ]
then
    python3 -m venv .venv
fi
source .venv/bin/activate
export PYTHONPATH=$script_path/src
EOF
direnv allow

pip3 install -r requirements.txt
echo end installing
}

case "$1"
in
install) install;;
esac
