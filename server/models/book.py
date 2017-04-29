import bcrypt
from ..db import query_db

class Book(object):

    def __init__(self, isbn, title, id=None, saved=False):
        self.isbn = isbn
        self.title = title
        self.id = id
        self.saved = saved

    def save(self):
        if not self.saved:
            query_db('INSERT INTO books (isbn,title) VALUES (?,?)',
                     (self.isbn, self.title))
            self = Book.with_isbn(self.isbn)

    @staticmethod
    def with_isbn(isbn):
        book = query_db('SELECT * FROM books WHERE isbn = ?',
                        (isbn,), one=True)

        if book is not None:
            return Book(book['isbn'], book['title'],
                        id=book['id'], saved=True)
        return None
