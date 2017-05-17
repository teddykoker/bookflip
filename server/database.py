from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database(object):

    def __init__(self, app=None):
        if app is not None:
            init_app(app)

    def init_app(self, app):
        self.engine = create_engine('sqlite:///' + app.config['DATABASE_URI'])
        self.session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=self.engine))

        self.Base = declarative_base()
        self.Base.query = self.session.query_property()


db = Database()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import book, listing, user

    db.Base.metadata.create_all(bind=engine)





