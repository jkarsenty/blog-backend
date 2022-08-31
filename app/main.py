from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse
from schemas import User, Article

app = FastAPI()

## Index Endpoint

@app.get("/", response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def index():
    '''Home Page, Display all endpoints infos'''
    
    with open('html/home.html', 'r',encoding="utf-8") as f: 
        home = f.read()
    
    return HTMLResponse(content=home)

## Login Endpoint

## Users Endpoints

@app.get("/users",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
def display_users_endpoints_infos() :
    '''Display all infos to interact with the users endpoints'''
    
    with open('html/users.html', 'r',encoding="utf-8") as f: 
        users_endpoints_infos = f.read()
    
    return HTMLResponse(content=users_endpoints_infos)


@app.get("/users/list")
def get_all_users():
    '''Get all users'''
    all_users = {}
    return all_users


@app.post("/users/create",status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    '''Create a new user'''
    return user


## Articles Endpoints

@app.get("/articles",response_class=HTMLResponse,status_code=status.HTTP_200_OK)
def display_articles_endpoints_infos() :
    '''Display all infos to interact with the articles endpoints'''

    with open('html/users.html', 'r',encoding="utf-8") as f: 
        articles_endpoints_infos = f.read()
    
    return HTMLResponse(content=articles_endpoints_infos)


@app.get("/articles/list")
def get_all_users():
    '''Get all articles'''
    all_articles = {}
    return all_articles


@app.post("/articles/create",status_code=status.HTTP_201_CREATED)
def create_article(article:Article):
    '''Create a new article'''
    return article