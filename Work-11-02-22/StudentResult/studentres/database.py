from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://root:root@localhost/pythonDB"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()
Session = sessionmaker(bind = engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)





