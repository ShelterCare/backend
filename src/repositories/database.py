from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values


configs = dotenv_values()
Base = declarative_base()

SQLALCHEMY_DATABASE_URL = (
    f"{configs['DRIVER']}://{configs['DB_USER']}:{configs['DB_PASSWORD']}"
    f"@{configs['DB_HOST']}:{configs['DB_PORT']}/{configs['DB_NAME']}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
