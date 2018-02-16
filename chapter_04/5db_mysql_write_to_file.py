#!/usr/bin/env/ python3
import csv
import MySQLdb
import sys

# CSV 입력 파일 경로와 파일명
output_file = sys.argv[1]

# MySQL 데이터베이스에 접속한다
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='hyunjoolee', passwd='1234qwer')
c = con.cursor()

# 파일 객체를 만들고, 헤더 행을 작성한다
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier_Name', 'Invoice_Number', 'Part_Number', 'Cost', 'Purchase_Date']
filewriter.writerow(header)

# Supplier 테이블을 검색하고 결과를 CSV 파일에 쓴다
c.execute("""SELECT * FROM Suppliers WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)
