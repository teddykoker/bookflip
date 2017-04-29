import bcrypt
from ..db import query_db

class Listing(object):

    def __init__(self, book_id, price, id=None, saved=False):
        self.book_id = book_id
        self.price = price
        self.id = id
        self.saved = saved

    def save(self):
        if not self.saved:
            query_db('INSERT INTO listings (book_id, price) VALUES (?,?)',
                     (self.book_id, self.price))
            self.saved = True

    @staticmethod
    def with_id(id):
        book = query_db('SELECT * FROM listings WHERE id = ?',
                        (id,), one=True)

        if book is not None:
            return Book(book['username'], book['email'], book['password'],
                        id=book['id'], saved=True)
        return None

