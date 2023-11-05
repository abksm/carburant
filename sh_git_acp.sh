#!/bin/bash

# Get the message from the command line argument
message="$1"

# Check if a message is provided
if [ -z "$message" ]; then
    message="-"
fi

# Add all changes
git add .

# Commit changes with the provided message
git commit -m "$message"

# Push changes to the remote repository
git push

echo "Changes committed and pushed with message: $message"
