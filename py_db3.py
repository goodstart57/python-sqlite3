"""
사용자로부터 입력을 받아서 게시물을 작성해주는 프로그램

> 게

> 제목을 입력해주세요 :
> 내용을 입력해 주세요 :
> 모든 게시물1
> 모든 게시물2
> 모든 게시물3
> ...
"""

import sqlite3

c = sqlite3.connect("test.sqlite3")
db = c.cursor()

this_title = input("제목을 입력해주세요 : ")
this_content = input("내용을 입력해주세요 : ")
sql_articles_insert_record = "INSERT INTO articles ('title', 'content') VALUES ('{}', '{}')".format(this_title, this_content)
db.execute(sql_articles_insert_record)
c.commit()

sql_articles_query_all = "SELECT * FROM articles"
db.execute(sql_articles_query_all)
data = db.fetchall()
for row in data:
    print("제목 :", row[1])
    print("내용 :", row[2], end="\n\n")
    
c.close()