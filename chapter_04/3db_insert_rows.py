#!/usr/bin/env python3
import csv
import sqlite3
import sys

# CSV 입력 파일의 경로와 피알명
input_file = sys.argv[1]

# 메모리에 SQLite3 데이터베이스를 만든다

con = sqlite3.connect(':memory:')
query= """CREATE TABLE IF NOT EXISTS sales
          (customer VARCHAR(20),
          product VARCHAR(40),
          amount FLOAT,
          date DATE)"""
con.execute(query)
con.commit()

# sales 테이블에 몇 줄의 데이터를 입력한다
data = [('이현주', '공책', 2.0, '2018-02-01'),
        ('김희진', '지우개', 5.0, '2017-12-31'),
        ('노안영', '책받침', 7.5, '2018-01-01'),
        ('이호성', '엽서', 4.5, '2017-12-10')]
for tuple in data:
    print(tuple)
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# CSV 파일을 읽고 특정 행의 데이터를 갱신한다
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    con.execute("UPDATE sales SET amount=?, date=? WHERE customer=?;", data)
con.commit()

# sales 테이블에 질의한다
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
