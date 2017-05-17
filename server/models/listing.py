from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import db


class Listing(db.Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book")

    def __init__(self, price):
        self.price = price

    def __repr__(self):
        return '<Listing>'

    def serialized(self):
        return {'book': self.book.serialized(), 'price': self.price}
