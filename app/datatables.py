from pydantic import BaseModel

class Article(BaseModel):
    article_id : str
    title: str
    body: str

class User(BaseModel):
    user_id : str
    name : str
    connect_id : str
    pwd : str # hash of the pwd 