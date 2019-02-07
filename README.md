# sqlite3 controller

## sqlite3 with python3

생성자로 sqlite3 database의 경로(파일명 포함)를 받으면 sqlite3 패키지를 이용하여 database를 읽어들어와서 sql 쿼리문을 작성하는 대신 python 함수로 database를 조작할 수 있는 클래스입니다.

`DbController`클래스의 인스턴스를 생성한 후 `query`메소드의 docstring으로 사용 예시를 볼 수 있으며 다음과 같습니다.

```python
"""query in python sqlite3
:args:
    q_type (str) -- ["select_all", "select", "create", "update", "delete"]
    t_name (str) -- table name
    condition (str) -- query condition
    *kwargs -- used to insert, update

:return:
    query result
    
:example:
    dbc = DbController("board.sqlite3")
    # select all
    dbc.query(q_type="select_all", t_name="articles", condition=None)
    # select 1
    dbc.query(q_type="select_one", t_name="articles", condition=None, n=1)
    # select n
    dbc.query(q_type="select", t_name="articles", condition=None, n=1)
    # create table
    dbc.query(q_type="create", t_name="articles", condition=None, title="TEXT", content="TEXT")
    # insert row
    dbc.query(q_type="insert", t_name="articles", condition=None, title="test dbc", content="test dbc")
    # update
    dbc.query(q_type="update", t_name="articles", condition="id=5", title="hi", content="wowowowowowow")
    dbc.query(q_type="select_all", t_name="articles", condition="id=5")
    # delete
    dbc.query(q_type="delete", t_name="articles", condition="id=5")
    dbc.query(q_type="select_all", t_name="articles", condition="id=5")
"""
```



### DbController 인스턴스 생성

```python
from db_controller import DbController

dbc = DbController("blog.db")
```



### blog.db의 모든 데이터 조회

```python
dbc.query(q_type="select_all", t_name="articles", condition=None)
```



### blog.db에서 title이 hi인 데이터 조회

```python
dbc.query(q_type="select_all", t_name="articles", condition="title='hi'")
```



### blog.db에서 새로운 레코드 생성

```python
dbc.query(q_type="insert", t_name="articles", condition=None, title="hi", content="hi everyone", author="goodstart57@gmail.com")
```



### blog.db에서 특정 레코드 제거

```python
dbc.query(q_type="delete", t_name="articles", condition="title='hi'")
```

