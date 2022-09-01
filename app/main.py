from typing import List
from fastapi import FastAPI, status, Depends, Response, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from passlib.context import CryptContext 

from . import schemas
from . import models
from .database import engine, SessionLocal


# launch database engine (create table)
models.Base.metadata.create_all(bind=engine)

# create app
app = FastAPI()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# hash password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

## Index Endpoint ##

@app.get("/", response_class=HTMLResponse,status_code=status.HTTP_200_OK, tags=["Home"])
async def index():
    '''Home Page, Display all endpoints infos'''
    
    with open('app/html/home.html', 'r',encoding="utf-8") as f: 
        home = f.read()
    
    return HTMLResponse(content=home)


## Login Endpoint ##

@app.post("/login", tags=["Login"])
def login(login : schemas.Login, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.login == login.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    good_pwd = pwd_context.verify(login.pwd, user.pwd)
    if not good_pwd :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")

    return user


## Users Endpoints ##

@app.get("/users/list", response_model=List[schemas.ShowUser], status_code=200, tags=["Users"])
def get_all_users(db : Session = Depends(get_db)):
    '''Get all users'''
   
    all_users = db.query(models.User).all()
   
    return all_users


@app.get("/users/list/{user_id}", response_model=schemas.ShowUser, status_code=200, tags=["Users"])
def get_one_user(user_id : int, db : Session = Depends(get_db)):
    '''Get user of id {user_id}'''
   
    one_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not one_user :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'User of id {user_id} does not exist')

    return one_user


@app.post("/users/create", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    '''Create a new user'''
    hashed_pwd = pwd_context.hash(user.pwd)

    new_user = models.User(
        name = user.name,
        login = user.login,
        pwd = hashed_pwd
        )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.delete('/users/delete/{user_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_one_user(user_id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id)
    
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'User of id {user_id} does not exist')

    user.delete(synchronize_session=False)
    db.commit()

    return f"User {user_id} Deleted"


## Articles Endpoints ##

@app.get("/articles/list", status_code=200, tags=["Articles"])
def get_all_articles(db : Session = Depends(get_db)):
    '''Get all articles'''
   
    all_articles = db.query(models.Article).all()
   
    return all_articles


@app.get("/articles/list/{article_id}", status_code=200, tags=["Articles"])
def get_one_article(article_id : int, db : Session = Depends(get_db)):
    '''Get article of id {article_id}'''
   
    one_article = db.query(models.Article).filter(models.Article.article_id == article_id).first()
    if not one_article :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'Article of id {article_id} does not exist')

    return one_article


@app.post("/articles/create",status_code=status.HTTP_201_CREATED, tags=["Articles"])
def create_article(article: schemas.Article, db : Session = Depends(get_db)):
    '''Create a new article'''
    
    new_article = models.Article(
        title = article.title,
        body = article.body
        )
    
    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


@app.delete('/articles/delete/{article_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Articles"])
def delete_one_article(article_id:int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.article_id == article_id)
    
    if not article.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'Article of id {article_id} does not exist')

    article.delete(synchronize_session=False)
    db.commit()

    return f"Article {article_id} Deleted"


# @app.put('/articles/update/{article_id}', status_code=status.HTTP_202_ACCEPTED, tags=["Articles"])
# def update_article(article_id:int, db: Session = Depends(get_db)):
#     article = db.query(models.Article).filter(models.Article.article_id == article_id)
    
#     if not article.first():
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'Article of id {article_id} does not exist')

#     article.update(synchronize_session=False)
#     db.commit()

#     return f"Article {article_id} Updated"