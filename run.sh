#!/bin/bash

# Navigate to the project directory
cd /home/loboguardian/Personal/lobo-steam.github.io || { echo "Failed to navigate to project directory"; exit 1; }

# Check if pipenv is installed
if ! command -v pipenv &> /dev/null
then
    echo "pipenv could not be found, please install it first."
    exit 1
fi

# Activate pipenv shell
pipenv shell || { echo "Failed to activate pipenv shell"; exit 1; }

# Check if reflex is installed
if ! command -v reflex &> /dev/null
then
    echo "reflex could not be found, please install it first."
    exit 1
fi

# Run the web server using reflex
reflex run || { echo "Failed to run reflex"; exit 1; }
