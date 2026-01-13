#!/bin/bash
# This script will help verify all pages after updates
echo "Checking all static HTML pages..."
cd /home/linkl0n/cert-projects/Car-Dealership/server/frontend/static/
for file in *.html; do
    echo "✓ Found: $file"
done
