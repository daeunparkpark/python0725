# db1.py

import sqlite3

#연결객체 생성
con = sqlite3.connect(":memory:")

#연결객체 생성 (일단은 메모리에서 연습)
con = sqlite3.connect(":memory:")
#커서객체
cur = con.cursor()
#테이블 구조 생성
cur.execute(" create table if not exists Phonebook " +
    " (id int primary key autoincrement, " +
    " name text, phoneNum text);" )
#1건 입력
cur.execute("insert into PhoneBook (name,phoneNum) values" +
    " ('홍길동','010-111');")

#입력파라메터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name,phoneNum) values" +
    " (?, ?);", (name, phoneNumber))

#다중의 행을 입력
datalist = (("이순신", "010-333"), ("박문수", "010-123"))
cur.executemany("insert into PhoneBook (name,phoneNum) values" +
    " (?, ?);", (name, datalist))

#검색구문
cur.execute("select * from PhoneBook;")
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(fetchmany(2))
print("---fetchall(2)---")
print(fetchall(2))

for row in cur:
    print(row)


