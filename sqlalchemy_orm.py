from sqlalchemy import create_engine

engine = create_engine("sqlite:///./data/books.db", echo=True, future=True)
from sqlalchemy.orm import Session

session = Session(engine)
from models import Author, Book
from sqlalchemy import select

stmt = select(Author)
for author in session.scalars(stmt):
    print(author)
stmt = select(Book)
for book in session.scalars(stmt):
    print(book)
for book in session.scalars(stmt):
    stmt = select(Book).join(Book.author).where(Author.last_name > "B")
for book in session.scalars(stmt):
    print(book)
stmt = select(Author).where(author.last_name == "King")
for author in session.scalars(stmt):
    print(author)
king = session.scalars(stmt).one()
stmt = select(Author).where(Author.last_name == "King")
king = session.scalars(stmt).one()
print(king)
king
king.append(Book(title="It"))
king.books.append(Book(title="It"))
stmt = select(Author).where(Author.last_name == "King").books()
stmt = select(Author).where(Author.last_name == "King").books
stmt = select(Author).where(Author.last_name == "King")
king = session.scalars(stmt).one()
print(king.books)
king = session.get(Author, 4)
print(king.books)
king.books.append(Book(title="Dead Zone"))
print(king.books)
king.books.remove(king.books[1])
print(king.books)
session.commit()
session.delete(king)
print(session.scalars(select(Book)).all())
session.rollback()
session.close()
import readline

for i in range(readline.get_current_history_length()):
    print(readline.get_history_item(i + 1))
