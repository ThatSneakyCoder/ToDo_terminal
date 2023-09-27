#!/bin/bash

COMMIT_MSG=$(git log -1 --pretty=%B)
echo "Commit Message: $COMMIT_MSG"

if [[ ! $COMMIT_MSG =~ ^\(commit[[:space]][0-9]+\)[[:space]].+$ ]]; then
  echo "Error: Commit message does not follow the correct format"
  exit 1
fi