#!/bin/bash

if [ ! -d "python-packagin-env" ]; then
    python -m venv python-packagin-env
fi

echo ""
read -n 1 -s -r -p "Press any key to continue"