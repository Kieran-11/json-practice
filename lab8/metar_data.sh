#!/bin/bash

# Define the URL
URL="https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85"

# Fetch the METAR data and save it to a temporary file
curl -s "$URL" > aviation.json

# Use jq to extract and display receiptTime values
jq -r '.features[]?.properties.receiptTime' aviation.json | head -n 6

