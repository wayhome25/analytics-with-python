#!/usr/bin/env python3
import csv
import sys

# 문제 : 인덱스 값 또는 열 헤더를 기반으로 열을 필터링하는 스크립트 중 하나를 수정하여 예제에서 필터링한 것과 다른 열을 출력하고, 출력 파일을 작성해보라
# 풀이 : supplier_data.csv 중에서 Invoice Number와 Cost 열의 값만을 따로 추출하여 파일로 작성한다.

input_file = sys.argv[1]
output_file = sys.argv[2]

column_name_list = ['Invoice Number', 'Cost']
column_index_list = []

with open(input_file, 'r', newline='') as input:
    with open(output_file, 'w', newline='') as output:
        file_reader = csv.reader(input)
        file_writer = csv.writer(output)
        header = next(file_reader)
        for name in column_name_list:
            column_index_list.append(header.index(name))

        file_writer.writerow(column_name_list)
        for row_list in file_reader:
            output_list = [row_list[idx] for idx in column_index_list]
            file_writer.writerow(output_list)
