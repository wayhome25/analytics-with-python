#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_colums = ['Invoice Number', 'Purchase Date']
my_colums_index = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        for idx, column in enumerate(header):
            if column in my_colums:
                my_colums_index.append(idx)

        filewriter.writerow(my_colums)
        for row_list in filereader:
            row_list_output = []
            for index in my_colums_index:
                row_list_output.append(row_list[index])
            filewriter.writerow(row_list_output)



