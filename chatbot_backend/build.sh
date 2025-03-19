#!/bin/bash

# Exit if any command fails
set -o errexit


cd chat_backend

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
