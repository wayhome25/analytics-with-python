li1 = ['a', 'b', 'c']
li2 = [1, 2, 3]
dic = dict()

for idx, key in enumerate(li1):
    if key not in dic:
        dic[key] = li2[idx]

print(dic)
