from pydantic import BaseModel

class Article(BaseModel):
    article_id : int
    title: str
    body: str

class User(BaseModel):
    user_id : int
    name : str
    connect_id : str
    pwd : str # hash of the pwd 