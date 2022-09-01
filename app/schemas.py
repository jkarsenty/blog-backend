from pydantic import BaseModel

class Article(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name : str
    login : str
    pwd : str # hash of the pwd 