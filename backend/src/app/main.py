import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker, Session

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise Exception("DATABASE_URL required.")
print(DATABASE_URL)

# SQLAlchemy engine.
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Database query builder.
database = Database(DATABASE_URL)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


origins = [
    "http://test.localhost.com",
    "https://mewslet.com",
    "https://www.mewslet.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base = declarative_base()

class TestObject(Base):
    __tablename__ = "testobjects"
    id = Column(Integer, primary_key=True)
    text = Column(String)

    def __repr__(self):
        return f"TestObject(text={self.text})"

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
session = SessionLocal()
obj = TestObject(text='testing')
session.add(obj)
session.commit()
session.close()


@app.get("/")
def root():
    return {"Data": [str(test) for test in SessionLocal().query(TestObject).all()]}