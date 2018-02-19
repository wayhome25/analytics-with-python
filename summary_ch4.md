# 4.2 MySQL 데이터베이스

## 준비사항

1. 데이터베이스 조회
SHOW DATABASES;


2. 데이터베이스 생성
CREATE DATABASE my_suppliers;


3. 데이터베이스 접속
USE my_suppliers;


4. 테이블 생성
CREATE TABLE IF NOT EXISTS Suppliers
  (Supplier_Name VARCHAR(20),
  Invoice_Number VARCHAR(20),
  Part_Number VARCHAR(20),
  Cost FLOAT, Purchase_Date DATE);


5. 테이블 조회
SHOW TABLES;


6. 테이블 구조보기
DESCRIBE Suppliers;


7. 사용자 생성
CREATE USER hyunjoolee@localhost IDENTIFIED BY '1234qwer';


8. 데이터베이스에 대한 사용자 권한 부여
GRANT ALL PRIVILEGES ON my_suppliers.* TO hyunjoolee@localhost;
FLUSH PRIVILEGES;


9. [mysqlclient](https://pypi.python.org/pypi/mysqlclient/1.3.12) 패키지 설치
파이썬이 MySQL 데이터베이스, 테이블과 상호작용할 수 있도록 도와주는 패키지
(psycopg2 : 파이썬이 postgres 데이터베이스, 테이블과 상호작용할 수 있도록 도와주는 패키지  - Python-PostgreSQL Database Adapter)


![screen 30](https://i.imgur.com/vLhXKVa.png)


## 테이블에 새 레코드 입력하기
- Supplier 테이블에 csv 파일 내용을 입력한다.

### Supplier 테이블 구조
![screen 31](https://i.imgur.com/UoJD7es.png)

### csv 파일 샘플

```
Supplier Name,Invoice Number,Part Number,Cost,Purchase Date
Supplier X,001-1001,2341,$500.00,1/20/14
Supplier X,001-1001,2341,$500.00,1/20/14
Supplier X,001-1001,5467,$750.00,1/20/14
Supplier X,001-1001,5467,$750.00,1/20/14
```

### 주요코드 (229p)

```python

# MySQL 데이터베이스 접속
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='hyunjoolee', passwd='1234qwer')

# 커서를 만들어서 my_suppliers 데이터베이스의 Suppliers 테이블에서 SQL 문을 실행하고 그 변화를 저장하는데 이용할 수 있게 한다.
c = con.cursor()

# 파일 읽기
# Suppliers 테이블에 데이터를 입력한다
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        if column_index < 4:
            # 날짜 이외의 컬럼은 데이터 내 양쪽 공백 , $, 콤마를 삭제한다.
            data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())

        else:
            # 날짜 컬럼은
            a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
            # datetime.strptime() : 날짜 형식의 string을 datetime 객체로 변환한다.
            a_date = a_date.strftime('%Y-%m-%d')
            # datetime.strftime() : datetime 객체를 새로운 형식의 string으로 변환한다.
            data.append(a_date)
    print(data)
    # ['Supplier X', '001-1001', '2341', '500.00', '2014-01-20']

    # 커서 객체의 execute 함수를 이용하여 Suppliers 테이블에 한 행의 변수들을 입력하기 위한 INSERT 문을 실행
    c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)

con.commit()
```

### 결과 확인

```code
mysql> SELECT * FROM Suppliers;
+---------------+----------------+-------------+------+---------------+
| Supplier_Name | Invoice_Number | Part_Number | Cost | Purchase_Date |
+---------------+----------------+-------------+------+---------------+
| Supplier X    | 001-1001       | 2341        |  500 | 2014-01-20    |
| Supplier X    | 001-1001       | 2341        |  500 | 2014-01-20    |
| Supplier X    | 001-1001       | 5467        |  750 | 2014-01-20    |
| Supplier X    | 001-1001       | 5467        |  750 | 2014-01-20    |
| Supplier Y    | 50-9501        | 7009        |  250 | 2014-01-30    |
| Supplier Y    | 50-9501        | 7009        |  250 | 2014-01-30    |
| Supplier Y    | 50-9505        | 6650        |  125 | 2014-02-03    |
| Supplier Y    | 50-9505        | 6650        |  125 | 2014-02-03    |
| Supplier Z    | 920-4803       | 3321        |  615 | 2014-02-03    |
| Supplier Z    | 920-4804       | 3321        |  615 | 2014-02-10    |
| Supplier Z    | 920-4805       | 3321        |  615 | 2014-02-17    |
| Supplier Z    | 920-4806       | 3321        |  615 | 2014-02-24    |
+---------------+----------------+-------------+------+---------------+
12 rows in set (0.00 sec)
```


## 테이블 내용 검색 및 csv 추출
- Supplier 테이블에서 Cost가 700 이상인 레코드를 검색한다.
- 이를 csv 파일로 따로 저장한다.

### 주요코드 (235p)

```python
# CSV 입력 파일 경로와 파일명
output_file = sys.argv[1]

# MySQL 데이터베이스에 접속한다
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='hyunjoolee', passwd='1234qwer')
c = con.cursor()

# 파일 객체를 만들고, 헤더 행을 작성한다
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier_Name', 'Invoice_Number', 'Part_Number', 'Cost', 'Purchase_Date']
filewriter.writerow(header)


# 커서 객체의 execute 함수를 이용하여 Suppliers 테이블에서 Cost 컬럼이 700을 초과하는 레코드를 가져오기 위한 SELECT문을 실행
c.execute("""SELECT * FROM Suppliers WHERE Cost > 700.0;""")
rows = c.fetchall()

# CSV 파일에 결과값을 입력
for row in rows:
    filewriter.writerow(row)
```

### 결과 확인
![screen 33](https://i.imgur.com/8Akw6hI.png)

## 테이블에 새 레코드 입력하기
- Supplier 테이블에서 임의 레코드를 업데이트
- 업데이트 내용은 csv 파일을 참고

### 업데이트용 csv 파일 샘플
- Supplier X, Supplier Y 의 Cost, Purchase_Date 를 각각 아래와 같이 변경
```
Cost,Purchase_Date,Supplier_Name
600,2014-01-22,Supplier X
200,2014-02-01,Supplier Y
```

### 주요코드 (237p)

```python

# CSV 파일을 읽고 특정 행을 갱신한다
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
header = next(file_reader)

for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    # ['600', '2014-01-22', 'Supplier X']

    # 커서 객체의 execute 함수를 이용하여 Suppliers 테이블에서 특정 Supplier_Name을 가진 모든 레코드의 Cost와 Purchase_Date를 수정
    c.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s;""", data)

# 데이터베이스에 저장    
con.commit()
```

### 결과확인
```
mysql> SELECT * FROM Suppliers;
+---------------+----------------+-------------+------+---------------+
| Supplier_Name | Invoice_Number | Part_Number | Cost | Purchase_Date |
+---------------+----------------+-------------+------+---------------+
| Supplier X    | 001-1001       | 2341        |  600 | 2014-01-22    |
| Supplier X    | 001-1001       | 2341        |  600 | 2014-01-22    |
| Supplier X    | 001-1001       | 5467        |  600 | 2014-01-22    |
| Supplier X    | 001-1001       | 5467        |  600 | 2014-01-22    |
| Supplier Y    | 50-9501        | 7009        |  200 | 2014-02-01    |
| Supplier Y    | 50-9501        | 7009        |  200 | 2014-02-01    |
| Supplier Y    | 50-9505        | 6650        |  200 | 2014-02-01    |
| Supplier Y    | 50-9505        | 6650        |  200 | 2014-02-01    |
| Supplier Z    | 920-4803       | 3321        |  615 | 2014-02-03    |
| Supplier Z    | 920-4804       | 3321        |  615 | 2014-02-10    |
| Supplier Z    | 920-4805       | 3321        |  615 | 2014-02-17    |
| Supplier Z    | 920-4806       | 3321        |  615 | 2014-02-24    |
+---------------+----------------+-------------+------+---------------+
12 rows in set (0.00 sec)
```
