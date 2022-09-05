import typer
import requests
from requests.structures import CaseInsensitiveDict

from .config import URL_APP

#app_login = typer.Typer()

#app_login.command()
def login(username:str, pwd:str):
    typer.echo(f"username : {username}")
    typer.echo(f"password : {pwd}")

    endpoint = "login"
    url = f"{URL_APP}/{endpoint}"
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    data = {
    "username": username,
    "pwd": pwd
    }

    resp = requests.post(url, headers=headers, json=data)

    typer.echo(resp.status_code)
    typer.echo(resp.json())


# if __name__ == "__main__":
#     app_login()