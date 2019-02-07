import sqlite3

c = sqlite3.connect("test.sqlite3")

db = c.cursor()
# sql = """
# CREATE TABLE articles (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     content TEXT
# )
# """
# print(sql)
# db.execute(sql)
# c.commit()
# db.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(db.fetchall()) # [('sqlite_sequence',), ('classmates',), ('users',), ('articles',)]

# sql2 = "INSERT INTO articles (title, content) VALUES ('해피 설', '세뱃돈 주세요')"
# db.execute(sql2)
# c.commit()

sql3 = "SELECT * FROM articles"
db.execute(sql3)
data = db.fetchall()
for row in data:
    print(row)
c.close()