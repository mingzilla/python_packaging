#!/bin/bash

if [ ! -d "python-packaging-env" ]; then
    python -m venv python-packaging-env
fi

echo ""
read -n 1 -s -r -p "Press any key to continue"