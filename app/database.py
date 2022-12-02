from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings
import time

SQLALCHEMY_DATABSE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:5432/{settings.database_name}"

# SQLALCHEMY_DATABSE_URL = f"postgresql://postgres:tushar9910@localhost:5432/social"


engine = create_engine(SQLALCHEMY_DATABSE_URL)

#  to communicate with databse
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# # # $ijhdfih
# while True:

#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="social",
#             user="postgres",
#             password="tushar9910",
#             cursor_factory=RealDictCursor,
#         )

#         cursor = conn.cursor()
#         print("Database has been connected")
#         break
#     except Exception as error:
#         print("connection with databse has been failed")
#         print(error)
#         time.sleep(2)
