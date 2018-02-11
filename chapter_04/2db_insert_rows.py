#!/usr/bin/env python3
import csv
import sqlite3
import sys

# CSV 입력 파일의 경로와 피알명
input_file = sys.argv[1]

# 메모리에 SQLite3 데이터베이스를 만든다
# 다섯 가지 속성을 지닌 Supplier 테이블을 만든다
con = sqlite3.connect('Supplier.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
                    (Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Number VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date DATE);"""
c.execute(create_table)
con.commit()

# CSV 파일을 읽는다
# 읽은 데이터를 Suppliers 테이블에 삽입한다
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
con.commit()
print('')

# Suppliers 테이블에 질의한다.
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
