from fastapi.testclient import TestClient
from .main import app
from .database import engine
from .config import USER_1, USER_2, ARTICLE_1, ARTICLE_2 
from .config import USER_WRONG_NAME_TYPE, USER_WRONG_LOGIN_TYPE,USER_WRONG_PWD_TYPE
from .config import ARTICLE_WRONG_BODY_TYPE, ARTICLE_WRONG_TITLE_TYPE

client = TestClient(app)

## Database Connection ##
def test_db_connection():
    assert engine.connect()


## Index ##
def test_index():
    response = client.get("/")
    assert response.status_code == 200


## Users ##
def test_create_user():
    response = client.post("/users/create",json=USER_1)
    assert response.status_code == 201
    assert response.json() == {"name": USER_1["name"], "login":USER_1["login"]}
    
    client.delete("/users/delete/1")

def test_delete_one_user():
    client.post("/users/create",json=USER_1)
    user_id = 1
    response = client.delete(f"/users/delete/{user_id}")
    assert response.status_code == 204
    
    user_id = 500
    response = client.delete(f"/users/delete/{user_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"User of id {user_id} does not exist"}

def test_get_all_users():

    client.post("/users/create",json=USER_1)
    client.post("/users/create",json=USER_2)
    
    response = client.get("/users/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json() == [
        {"name": USER_1["name"], "login":USER_1["login"]},
        {"name": USER_2["name"], "login":USER_2["login"]}
    ]

    client.delete("/users/delete/1")
    client.delete("/users/delete/2")


def test_get_one_user():
    client.post("/users/create",json=USER_1)
    user_id = 1
    response = client.get(f"/users/list/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"name": USER_1["name"], "login":USER_1["login"]}
    
    user_id = 500
    response = client.get(f"/users/list/{user_id}")
    assert response.status_code == 404
    assert response.json() == {"detail":f"User of id {user_id} does not exist"}

    client.delete("/users/delete/1")

## Articles ##
def test_create_article():
    response = client.post("/articles/create",json=ARTICLE_1)
    assert response.status_code == 201
    assert response.json() == {"article_id":1, "title":ARTICLE_1["title"], "body":ARTICLE_1["body"]}
    
    client.delete("/articles/delete/1")

def test_delete_one_article():
    client.post("/articles/create",json=ARTICLE_1)
    article_id = 1
    response = client.delete(f"/articles/delete/{article_id}")
    assert response.status_code == 204
    
    article_id = 500
    response = client.delete(f"/articles/delete/{article_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Article of id {article_id} does not exist"}

def test_get_all_articles():
    client.post("/articles/create",json=ARTICLE_1)
    client.post("/articles/create",json=ARTICLE_2)
    
    response = client.get("/articles/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json() == [
        {"article_id":1,"title": ARTICLE_1["title"], "body":ARTICLE_1["body"]},
        {"article_id":2,"title": ARTICLE_2["title"], "body":ARTICLE_2["body"]}
    ]

    client.delete("/articles/delete/1")
    client.delete("/articles/delete/2")

def test_get_one_article():
    client.post("/articles/create",json=ARTICLE_1)
    article_id = 1
    response = client.get(f"/articles/list/{article_id}")
    assert response.status_code == 200
    assert response.json() == {"article_id":1,"title": ARTICLE_1["title"], "body":ARTICLE_1["body"]}
    
    article_id = 500
    response = client.get(f"/articles/list/{article_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Article of id {article_id} does not exist"}

    client.delete("/articles/delete/1")


## Login ##
def test_login():
    pass

