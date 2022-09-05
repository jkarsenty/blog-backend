import typer
import requests
from requests.structures import CaseInsensitiveDict

URL_APP = "http://www.localhost:8000"

#app_users = typer.Typer()

#@app_users.command()
def create_user(name:str, login:str, pwd:str):
    typer.echo("Creating User ...")
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

    typer.echo(resp.status_code)
    typer.echo(resp.json())
    typer.echo("User Created")


#@app_users.command()
def get_all_users():
    typer.echo("Getting all users ...")
    
    endpoint = "users/list"
    url = f"{URL_APP}/{endpoint}"
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    typer.echo(resp.status_code)
    typer.echo(resp.json())


#@app_users.command()
def get_one_user(user_id:int):
    typer.echo(f"Getting user {user_id} ...")

    endpoint = "users/list"
    url = f"{URL_APP}/{endpoint}/{user_id}"
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    typer.echo(resp.status_code)
    if resp.status_code == 200 :
        typer.echo(resp.json())
    else :
        typer.echo(f'User of id {user_id} does not exist')


#@app_users.command()
def delete_one_user(user_id:int):
    typer.echo(f"Deletting user {user_id} ...")
    
    endpoint = "users/delete"
    url = f"{URL_APP}/{endpoint}/{user_id}"

    headers = CaseInsensitiveDict()
    headers["accept"] = "*/*"


    resp = requests.delete(url, headers=headers)
    
    typer.echo(resp.status_code)
    if resp.status_code == 204 :
        typer.echo(f"User of id {user_id} deleted")
    elif resp.status_code == 404 :
        typer.echo(f'User of id {user_id} does not exist')


# if __name__ == "__main__":
#     app_users()