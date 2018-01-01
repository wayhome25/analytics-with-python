#!/usr/bin/env python3
import csv
import sys

# 문제 : 조건, 집합, 또는 정규 표현식에 따라 행을 필터링하는 스크립트 중 하나를 수정하여 예제에서 필터링한 것과 다른 행을 출력하고, 출력 파일을 작성해보라.
# 풀이 : 입력 파일 중 Part Number가 7009 이거나 혹은 Cost가 $500.00 이상인 값을 출력하는 파일을 작성한다

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as input_file:
    with open(output_file, 'w', newline='') as output_file:
        file_reader = csv.reader(input_file)
        file_writer = csv.writer(output_file)

        header = next(file_reader)
        file_writer.writerow(header)

        for row_list in file_reader:
            part_number = row_list[2]
            cost = float(row_list[3].strip('$'))
            if part_number == '7009' or cost >= 500.00:
                file_writer.writerow(row_list)

