import typer
import requests
from requests.structures import CaseInsensitiveDict

URL_APP = "http://www.localhost:8000"

app = typer.Typer()

@app.command()
def create_user(name:str, login:str, pwd:str):
    typer.echo(f"name : {name}")
    typer.echo(f"login : {login}")
    typer.echo(f"pwd : {pwd}")

    endpoint = "users/create"
    url = f"{URL_APP}/{endpoint}"
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    data ={
        "name": name,
        "login": login,
        "pwd": pwd
    }

    resp = requests.post(url, headers=headers, json=data)

    print(resp.status_code)
    print(resp.json())


@app.command()
def get_all_users():
    typer.echo("All Users")
    
    endpoint = "users/list"
    url = f"{URL_APP}/{endpoint}"

    resp = requests.get(url)

    print(resp.status_code)
    print(resp.json())


@app.command()
def get_one_user(user_id:int):
    typer.echo(f"User {user_id}")

    endpoint = "users/list"
    url = f"{URL_APP}/{endpoint}/{user_id}"

    resp = requests.get(url)

    print(resp.status_code)
    print(resp.json())


@app.command()
def delete_one_user(user_id:int):
    typer.echo(f"User {user_id} deleted")
    
    endpoint = "users/delete"
    url = f"{URL_APP}/{endpoint}/{user_id}"

    headers = CaseInsensitiveDict()
    headers["accept"] = "*/*"


    resp = requests.delete(url, headers=headers)

    print(resp.status_code)


if __name__ == "__main__":
    app()