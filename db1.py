import sqlite3

#메모리 상에 DB를 생성
conn = sqlite3.connect(":memory:")

#커서 생성
cur = conn.cursor()

#테이블 생성
cur.execute("CREATE TABLE PhoneBook (Name text, PhoneNum text);")

#1건 입력
cur.execute("INSERT INTO PhoneBook VALUES ('Derick', '010-1234-5678');")

#입력 파라메터로 받기
name = "Kent"
phoneNumber = "010-1234-5678"
cur.execute("INSERT INTO PhoneBook VALUES(?, ?);", (name, phoneNumber))

#여러건 입력
datalist = (("Tom", "010-1234-5678"), ("Daisy", "010-1234-5678"))
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?);", datalist)        


#전체 조회
cur.execute("SELECT * FROM PhoneBook;")
# for row in cur:
#     print(row[0], row[1])

#패티 메소드
print("---fetchone()---")
print(cur.fetchone())

print("---fetchmany(2)---")
print(cur.fetchmany(2))

print("---fetchall()---")
print(cur.fetchall())

cur.execute("SELECT * FROM PhoneBook;")
print("---fetchall()---")
print(cur.fetchall())