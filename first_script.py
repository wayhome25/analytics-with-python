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
# input_path = sys.argv[1]
# for input_file in glob.glob(os.path.join(input_path, '*.txt')):
#     with open(input_file, 'r') as filereader:
#         for row in filereader:
#             print(row.strip())

# 파일 작성하기
# 하나의 텍스트 파일 작성하기
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')

for index_value in range(max_index):
    if index_value < max_index - 1:
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print('Output written to file')

# CSV파일 작성하기 
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
output_file = sys.argv[1]

with open(output_file, 'a') as filewriter:
    for index_value in range(max_index):
        filewriter.write(str(my_numbers[index_value])+',')

    filewriter.write('\n')

print('Output appended to file')

