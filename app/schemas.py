from pydantic import BaseModel

class Article(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name : str
    login : str
    pwd : str # hash of the pwd 

class ShowUser(BaseModel):
    name : str
    login : str

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    pwd : str