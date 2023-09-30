#!/bin/bash

for file in $(find . -name "*.py"); do
  line_count=$(wc -l < "$file")

  if [ "$line_count" -gt 120 ]; then
    echo "Violation: $file has more than 120 lines."
    exit 1
  fi
done

echo "Success: All python files have 120 lines or less"

for file in $(find ./scripts -type f); do
  line_count=$(wc -l < "$file")

  if [ "$line_count" -gt 25 ]; then
    echo "VIOLATION: $file has more than 20 lines"
    exit 1
  fi
done

echo "SUCCESS: All .sh files are shorter than 20 lines"