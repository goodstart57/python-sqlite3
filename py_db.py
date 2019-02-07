"""sqlite3 in python
1. sqlite3에 접속
2. table 관련 SQL 작성 (CREATE TABLE)
3. CRUD(Create, Read, Update, Delete) SQL
"""
import sqlite3

# sqlite3 test.sqlite3
conn = sqlite3.connect("test.sqlite3")
cur = conn.cursor() # create cursor
cur.execute("SELECT * FROM users LIMIT 10") # write sql script => execute()
data = cur.fetchall() # run cursor => fetchone(), fetchall()
for row in data:
    print(row)

# cur.execute("PRAGMA table_info(users)")
# colnames = cur.fetchall()
# for col in colnames:
#     print(col)
# colnames = list(map(lambda x: x[1], colnames))
# print(colnames) # ['id', 'first_name', 'last_name', 'age', 'country', 'phone', 'balance']

'''
실습 1. CREATE
내 정보를 한 행(레코드)으로 만들어 보기

Create & Update & Delete의 경우 -> conn.commit()
Read는 필요 없다.
'''
# users_colnames = "('id', 'first_name', 'last_name', 'age', 'country', 'phone', 'balance')"
# my_input_data = "('1001', '재서', '이', '27', '울산광역시', '010-9399-3170', '7000000000')"
# cur.execute("INSERT INTO users {} VALUES {}".format(users_colnames, my_input_data))

cur.execute("SELECT * FROM users WHERE first_name = '재서'")
print("재서를 찾아라!")
for row in cur.fetchall():
    print(row)
