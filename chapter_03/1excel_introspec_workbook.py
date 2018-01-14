#!/usr/bin/env python3
import sys
from xlrd import open_workbook


input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)

for worksheet in workbook.sheets():
    print("worksheet name: {} \tRows: {} \tColumns: {}".format(worksheet.name, worksheet.nrows, worksheet.ncols))


