import sys

li = [[1,2], [3,4], [5,6]]

# output_file = sys.argv[1]
# max_idx1 = len(li) - 1
# max_idx2 = len(li[0]) - 1
# with open(output_file, 'w') as f:
#     for i in range(len(li)):
#         for j in range((len(li[0]))):
#             if i == max_idx1 and j == max_idx2:
#                 f.write(str(li[i][j])+'\n')
#             else:
#                 f.write(str(li[i][j])+',')
# print('end')

list_of_lists = [['a', 'b'], ['hi', 'hello']]
output = ''

for li in list_of_lists:
    max_index = len(li)
    for index in range(max_index):
        if index < max_index - 1:
            output += str(li[index]) + ','
        else:
            output += str(li[index]) + '\n'

print(output)
