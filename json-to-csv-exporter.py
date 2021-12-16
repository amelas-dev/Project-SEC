#!/usr/bin/env python3

# Place this Python script in your working directory when you have JSON files in a subdirectory.
# To run the script via command line: "python3 json-to-csv-exporter.py"

import json
import glob
from datetime import datetime
import csv

# Place your JSON data in a directory named 'data/'
src = "data/"

date = datetime.now()
data = []

# Change the glob if you want to only look through files with specific names
files = glob.glob('data/*', recursive=True)

# Loop through files

for single_file in files:
  with open(single_file, 'r') as f:

    # Use 'try-except' to skip files that may be missing data
    try:
      json_file = json.load(f)
      data.append([
        json_file['entityName'],
        json_file['fetchTime'],
        json_file['categories']['performance']['score'],
        json_file['audits']['largest-contentful-paint']['numericValue'],
        json_file['audits']['speed-index']['numericValue'],
        json_file['audits']['max-potential-fid']['numericValue'],
        json_file['audits']['cumulative-layout-shift']['numericValue'],
        json_file['audits']['first-cpu-idle']['numericValue'],
        json_file['audits']['total-byte-weight']['numericValue']
      ])
    except KeyError:
      print(f'Skipping {single_file}')

# Sort the data
data.sort()

# Add headers
data.insert(0, ['entityName'])

# Export to CSV.
# Add the date to the file name to avoid overwriting it each time.
csv_filename = f'{str(date)}.csv'
with open(csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Updated CSV")