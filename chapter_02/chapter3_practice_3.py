#!/usr/bin/env python3
import csv
import glob
import os
import sys

# 문제 : 우선 폴더에서 새로운 csv 입력 파일들을 만들고 별도의 출력 폴더를 만든다.
# 여러개의 파일을 처리하는 스크립트 중 하나를 사용하여 새로운 입력파일들을 처리하고 그 결과를 출력 파일로 만들어 해당 출력 폴더에 저장해보라.

# 풀이 : deal_1.csv, deal_2.csv, deal_3.csv 을 하나의 파일로 합친 deal.csv 파일을 만들어서 저장한다.

input_path = sys.argv[1]
output_file = sys.argv[2]
files = glob.glob(os.path.join(input_path, 'deal_*.csv'))

header_exist = False

for file in files:
    with open(file, 'r', newline='') as input:
        with open(output_file, 'a', newline='') as output:
            file_reader = csv.reader(input, delimiter=';')
            file_writer = csv.writer(output, delimiter=';')
            header = next(file_reader)
            if not header_exist:
                file_writer.writerow(header)
                header_exist = True
                print(header)
            for row in file_reader:
                file_writer.writerow(row)
                print(row)

