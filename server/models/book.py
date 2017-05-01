import bcrypt
from ..db import query_db

class Book(object):
    def __init__(self, id):
        self._id = id


    @property
    def id(self):
        return self._id


    @property
    def isbn(self):
        return query_db('SELECT isbn FROM books WHERE id = ?',
                        (self.id,), one=True)['isbn']

    @property
    def title(self):
        return query_db('SELECT title FROM books WHERE id = ?',
                        (self.id,), one=True)['title']


    def serialized(self):
        return {'title': self.title, 'isbn': self.isbn}


    @staticmethod
    def add(isbn, title):
        query_db('INSERT INTO books (isbn,title) VALUES (?,?)',
                 (isbn, title))

    @staticmethod
    def all():
        books = query_db('SELECT id FROM listings')
        for book in books:
            yield Book(book['id'])


    @staticmethod
    def with_isbn(isbn):
        book = query_db('SELECT id FROM books WHERE isbn = ?',
                      (isbn,), one=True)
        if book is not None:
            return Book(book['id'])
        return None


    @staticmethod
    def with_title(title):
        book = query_db('SELECT id FROM books WHERE title = ?',
                      (user,), one=True)
        if book is not None:
            return Book(book['id'])
        return None
