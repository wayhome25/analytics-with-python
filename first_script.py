import sys
import glob
import os

# 파일 읽기
# 하나의 텍스트 파일 읽기
#input_file = sys.argv[1]
#with open(input_file, 'r') as filereader:
#    for row in filereader:
#        print(row.strip())

# 다수의 파일 읽기 
input_path = sys.argv[1]
for input_file in glob.glob(os.path.join(input_path, '*.txt')):
    with open(input_file, 'r') as filereader:
        for row in filereader:
            print(row.strip())
