from turtle import home
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse
from datatables import User, Article

app = FastAPI()

## Index Endpoint

@app.get("/", response_class=HTMLResponse,status_code=status.HTTP_200_OK)
async def index():
    '''Home Page'''

    home = """
    <html>
        <head>
            <title>Blog Backend</title>
        </head>
        <body>
            <h1>Welcome in our Blog Backend</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=home)



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


@app.post("/users/create",status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    '''Create a new user'''
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


@app.post("/articles/create",status_code=status.HTTP_201_CREATED)
def create_article(article:Article):
    '''Create a new article'''
    return article