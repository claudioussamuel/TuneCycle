#!/bin/bash

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install system dependencies if needed (optional)
# apt-get update && apt-get install -y some-system-library

echo "Build complete!"

