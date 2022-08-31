from fastapi import FastAPI
from datatables import User, Article

app = FastAPI()

## Users Endpoints

@app.get("/users")
def display_users_endpoints_infos() :
    '''Display all infos to interact with the users endpoints'''
    users_endpoints_infos = {}

    return users_endpoints_infos


@app.get("/users/list")
def get_all_users():
    '''Get all users'''
    all_users = {}
    return all_users


@app.post("/users/create")
def create_user(user: User):
    return user


## Articles Endpoints

@app.get("/articles")
def display_articles_endpoints_infos() :
    '''Display all infos to interact with the articles endpoints'''
    articles_endpoints_infos = {}

    return articles_endpoints_infos


@app.get("/articles/list")
def get_all_users():
    '''Get all articles'''
    all_articles = {}
    return all_articles


@app.post("/articles/create")
def create_article(article:Article):
    return article