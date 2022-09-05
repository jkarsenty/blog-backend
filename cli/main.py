import typer
from functions.login import login
from functions.users import create_user, get_all_users, get_one_user, delete_one_user
from functions.articles import create_article, get_all_articles, get_one_article, delete_one_article

app = typer.Typer()

## Login ##
@app.command()
def login(username:str, pwd:str):
    login(username, pwd)


## Users ##
@app.command()
def create_user(name:str, login:str, pwd:str):
    create_user(name,login,pwd)

@app.command()
def get_all_users():
    get_all_users()

@app.command()
def get_one_user(user_id:int):
    get_one_user(user_id)

@app.command()
def delete_one_user(user_id:int):
    delete_one_user(user_id)


## Articles ##
@app.command()
def create_article(title:str, body:str):
    create_article(title, body)

@app.command()
def get_all_articles():
    get_all_articles()

@app.command()
def get_one_article(article_id:int):
    get_one_article(article_id)

@app.command()
def delete_one_article(article_id:int):
    delete_one_article(article_id)


if __name__ == "__main__":
    app()