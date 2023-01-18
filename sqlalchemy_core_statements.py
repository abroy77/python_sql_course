from sqlalchemy import create_engine

engine = create_engine("sqlite:///./books.db", echo=True, future=True)
conn = engine.connect()
# MetaData
from sqlalchemy import MetaData, Table

metadata = MetaData()
author_table = Table("author", metadata, autoload_with=engine)
author_table
# select
from sqlalchemy import select

stmt = select(author_table).where(author_table.c.first_name == "Stephen")
stmt
print(stmt)
result = conn.execute(stmt)
print(result.all())
print(select(author_table))
print(select(author_table.c.first_name, author_table.c.last_name))

result = conn.execute(stmt)
print(result.all())
str(stmt)
compiled = stmt.compile()
str(compiled)
compiled.params
result = conn.execute(compiled)
print(result.all())
stmt = select(author_table).where(
    author_table.c.last_name > "B", author_table.c.first_name > "S"
)
str(stmt)
result = conn.execute(stmt)
print(result.all())
# INSERT
from sqlalchemy import insert

stmt = insert(author_table).values(first_name="Richard", last_name="Bachman")
str(stmt)
conn.execute(stmt)
conn.execute(select(author_table)).all()
result = conn.execute(
    insert(author_table),
    [
        {"first_name": "John", "last_name": "Le Carre"},
        {"first_name": "Alex", "last_name": "Michaelides"},
    ],
)
conn.commit()
conn.execute(select(author_table)).all()
# Update
from sqlalchemy import update

stmt = (
    update(author_table)
    .where(author_table.c.last_name == "King")
    .values(first_name="Stephen", last_name="The Ruler")
)
conn.execute(stmt)
conn.execute(select(author_table)).all()
conn.rollback()
conn.execute(select(author_table)).all()
# Delete
from sqlalchemy import delete

stmt = delete(author_table).where(author_table.c.author_id == 7)
conn.execute(stmt)
conn.execute(select(author_table)).all()
conn.rollback()
conn.execute(select(author_table)).all()
import readline

for i in range(readline.get_current_history_length()):
    print(readline.get_history_item(i + 1))
