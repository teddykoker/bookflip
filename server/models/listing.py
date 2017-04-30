import bcrypt
from ..db import query_db
from book import Book

class Listing(object):

    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id


    @property
    def book(self):
        book_id = query_db('SELECT book_id FROM listings WHERE id = ?',
                           (self.id,), one=True)['book_id']
        return Book(book_id)


    @property
    def price(self):
        return query_db('SELECT price FROM listings WHERE id = ?',
                        (self.id,), one=True)['price']


    def serialized(self):
        return {'book': self.book.serialized(), 'price': self.price}


    @staticmethod
    def add(book, price):
        query_db('INSERT INTO listings (book_id,price) VALUES (?,?)',
                 (book.id, price))

    @staticmethod
    def all():
        listings = query_db('SELECT id FROM listings')
        for listing in listings:
            yield Listing(listing['id'])
