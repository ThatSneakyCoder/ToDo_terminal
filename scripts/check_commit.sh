#!/bin/bash

COMMIT_MSG=$(git log -1 --pretty=%B)
echo "Commit Message: $COMMIT_MSG"

echo "$COMMIT_MSG" | grep -Pq "^\(commit\s+[0-9]+\)\s+.*$"

# Check the exit code of grep
if [ $? -ne 0 ]; then
  echo "Error: Commit message does not follow the correct format."
  exit 1
fi