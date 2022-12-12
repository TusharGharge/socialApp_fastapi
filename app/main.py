# from lib2to3.pytree import Base
# from http.client import HTTPException
# import email
from hashlib import new
from multiprocessing.sharedctypes import synchronized
from os import sync
from random import randrange
from passlib.context import CryptContext

# from sqlite3 import Cursor, connect
# import time
# from typing import Optional, List
# from fastapi import FastAPI, Depends, status, Request, Response, HTTPException
# from fastapi import Body
# from pydantic import BaseModel
# import psycopg2
# from psycopg2.extras import RealDictCursor

from .database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, utils

# from sqlalchemy.orm import Session
# import time
from fastapi import FastAPI
from .routers import post, users, auth, votes

import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings
import time

# imnportant line to coonect with database using sqlalchemy
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# it is use for call api from specific web
origins = ["https://www.google.com", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


my_posts = [
    {"title": "title of first 1", "content": "data of first post1 ", "id": 1},
    {"title": "title of first 1", "content": "data of first post1 ", "id": 1},
]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/d")
def root():
    return {"hello world"}
