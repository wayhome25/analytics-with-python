# 연속된 행 선택하기
- 불필요한 행을 제외하고 선택하는 방법

## 4행에서 16행까지 데이터만 가져와보자!

![screen 5](https://i.imgur.com/WxwTiLJ.png)

### 기본 파이썬
- 주요 코드 (133p)

```python
filereader = csv.reader(csv_in_file)  # 읽기용 파일
filewriter = csv.writer(csv_out_file) # 쓰기용 파일

row_counter = 1

for row in filereader: # 읽기용 파일 내용을 한줄씩 읽으면서
  if row_counter >= 4 and row_counter <= 16:  # 4행 ~ 16행 사이일때만
    filewriter.writerow(row)  # 쓰기용 파일에 한줄씩 입력한다.

    row_counter = row_counter + 1  # 그 다음줄 행번호
```

### 팬더스
- 주요 코드 (134p)

```python
data_frame = pd.read_csv(input_file, header=None)
data_frame = data_frame.drop([0,1,2,16,17,18])  # 지정한 행번호만 삭제한다.

data_frame.to_csv(output_file, index=False)

```

![screen 4](https://i.imgur.com/TlzVPEW.png)

# 헤더 추가하기

## 첫번째 행에 열 헤더를 추가해보자!
![screen 6](https://i.imgur.com/JfkAeHv.png)

### 기본 파이썬
- 주요 코드 (136p)

```python
filereader = csv.reader(csv_in_file)  # 읽기용 파일
filewriter = csv.writer(csv_out_file) # 쓰기용 파일

# 추가할 열 헤더 리스트
header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']

# 쓰기용 파일에 한줄 쓰기
filewriter.writerow(header_list)

# 읽기용 파일을 한줄씩 읽으면서, 쓰기용 파일에 한줄씩 쓰기
for row in filereader:
  filewriter.writerow(row)
```

### 팬더스
- 주요 코드 (137p)

![screen 7](https://i.imgur.com/rQ7jS3X.png)


# 여러 파일의 데이터 합치기

## 파일 여러개를 하나로 합쳐보자!
- sales_february_2014.csv
- sales_january_2014.csv
- sales_march_2014.csv

### 기본 파이썬
- 주요 코드 (143p)

![screen 8](https://i.imgur.com/eUIKiPR.png)


### 팬더스
- 주요 코드 (146p)

![screen 10](https://i.imgur.com/HCiUBWJ.png)

# 연습문제

1. 조건, 집합, 또는 정규 표현식에 따라 행을 필터링 하는 스크립트 중 하나를 수정하여 예제에서 필터링한 것과 다른 행을 출력하고, 출력 파일을 작성해보라

```python
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

```

2. 인덱스 값 또는 열 헤더를 기반으로 열을 필터링하는 스크립트 중 하나를 수정하여 예제에서 필터링한 것과 다른 열을 출력하고, 출력 파일을 작성해보라

```python
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

```

3. 우선 폴더에서 새로운 csv 입력 파일들을 만들고 별도의 출력 폴더를 만든다. 여러개의 파일을 처리하는 스크립트 중 하나를 사용하여 새로운 입력파일들을 처리하고 그 결과를 출력 파일로 만들어 해당 출력 폴더에 저장해보라.

```python
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


```
