#!/bin/bash
#
# Start a console application, by running 'main.py'
#
# Usage:
#
#   ./scripts/run_console.sh
#
#
#
if [[ "$PWD" =~ scripts$ ]]; then
    echo "Please run the script from the project root. "
    echo "Present working director: $PWD"
    echo " "
    echo "Tip: like this"
    echo " "
    echo "./scripts/run_console.sh"
    exit 42
fi

# Install the package from the local code
./scripts/install_this_package.sh

# Run the code
python3 main.py
