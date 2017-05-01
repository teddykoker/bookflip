from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..database import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    isbn = Column(String(13), unique=True)
    title = Column(String(128))
    listings = relationship("Listing", back_populates="book")


    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title


    def __repr__(self):
        return '<Book %r>' % (self.title)


    def serialized(self):
        return {'title': self.title, 'isbn': self.isbn}
