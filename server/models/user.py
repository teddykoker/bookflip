
from ..db import query_db


def all_users():
    return query_db('SELECT * FROM users')