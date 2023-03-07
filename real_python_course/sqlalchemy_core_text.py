# Connecting
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///./data/books.db", echo=True, future=True)
conn = engine.connect()
result = conn.execute(text("select * from author"))
result.dtype
print(result.all())
# commits
conn.execute(
    text("insert into author (first_name, last_name) values (:fn, :ln)"),
    [{"fn": "Tom", "ln": "Clancy"}, {"fn": "Stephen", "ln": "King"}],
)
print(result.all())
result = conn.execute(text("select * from author"))
print(result.all())
conn.commit()
# Rollbacks
conn.execute(
    text("insert into author (first_name, last_name) values (:fn, :ln)"),
    [{"fn": "Not", "ln": "Anauthor"}],
)
result = conn.execute(text("select * from author"))
print(result.all())
conn.rollback()
result = conn.execute(text("select * from author"))
print(result.all())
# Query results
result = conn.execute(text("select * from author"))
for row in result:
    print(f"{row.last_name}, {row.first_name}")
print(result.all())
result = conn.execute(text("select first_name, last_name  from author"))
for first_name, last_name in result:
    print(f"{first_name}, {last_name}")
result = conn.execute(text("select first_name, last_name  from author"))

for row in result:
    print(row[1])
result = conn.execute(text("select first_name, last_name  from author"))
for dict_row in result.mappings():
    print(dict_row)
# Parameters
result = conn.execute(
    text(" select last_name from author where last_name > :ln"), {"ln": "C"}
)
print(result.all())
stmt = text(" select last_name from author where last_name > :ln")
stmt
stmt = stmt.bindparams(ln="C")
result = conn.execute(stmt)
print(result.all())
stmt = text(" select last_name from author where last_name > :ln")
stmt = stmt.bindparams(ln="B")
result = conn.execute(stmt)
print(result.all())
# cleanup
conn.close()
# don't use dynamic f-strings for querying
# only run commands
