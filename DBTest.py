import sqlite3
#test.db 파일이 있으면 연결, 없으면 생성
con = sqlite3.connect(r"c:\work\sample2.db")

#커서 객체를 리턴
cursor = con.cursor()
#데이터 조회
cursor.execute("SELECT * FROM Employee")
for row in cursor.fetchall():
    print(row)

con.close()

