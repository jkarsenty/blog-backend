from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    login = Column(String, unique=True)
    pwd = Column(String)


class Article(Base):
    __tablename__ = "articles"

    article_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)