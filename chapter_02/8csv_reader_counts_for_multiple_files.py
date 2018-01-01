#!/usr/bin/env python3
import csv
import glob
import os
import sys

input_path = sys.argv[1]

file_counter = 0
files = glob.glob(os.path.join(input_path, 'sales_*'))

for input_file in files:
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            row_counter += 1
    print('{}: \t{} rows \t{} columns'.format(os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1

print('Number of files: {}'.format(file_counter))
