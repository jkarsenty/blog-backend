import typer
from functions import login_user
from functions import users
from functions import articles

app = typer.Typer()

## Login ##
@app.command()
def login(username:str, pwd:str):
    login_user.login(username, pwd)


## Users ##
@app.command()
def create_user(name:str, login:str, pwd:str):
    users.create_user(name,login,pwd)

@app.command()
def get_all_users():
    users.get_all_users()

@app.command()
def get_one_user(user_id:int):
    users.get_one_user(user_id)

@app.command()
def delete_one_user(user_id:int):
    users.delete_one_user(user_id)


## Articles ##
@app.command()
def create_article(title:str, body:str):
    articles.create_article(title, body)

@app.command()
def get_all_articles():
    articles.get_all_articles()

@app.command()
def get_one_article(article_id:int):
    articles.get_one_article(article_id)

@app.command()
def delete_one_article(article_id:int):
    articles.delete_one_article(article_id)


if __name__ == "__main__":
    app()