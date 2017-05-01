from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import app

engine = create_engine('sqlite:///' + app.config['DATABASE_URI'], echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import book, listing, user

    Base.metadata.create_all(bind=engine)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

