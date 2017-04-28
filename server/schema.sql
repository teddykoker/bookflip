
-- schema.sql


CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE listings (
  id INTEGER PRIMARY KEY,
  book_id INTEGER NOT NULL,
  price DECIMAL NOT NULL
);

CREATE TABLE books (
  id INTEGER PRIMARY KEY,
  isbn TEXT NOT NULL,
  title TEXT NOT NULL
);

/*

CREATE TABLE authors (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

-- references between books and authors
CREATE TABLE authors_books (
  author_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL
);

*/
