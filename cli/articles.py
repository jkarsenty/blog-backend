import typer
import requests
from requests.structures import CaseInsensitiveDict

URL_APP = "http://www.localhost:8000"

app = typer.Typer()

@app.command()
def create_article(title:str, body:str):
    print(f"title : {title}")
    print(f"body : {body}")

    endpoint = "articles/create"
    url = f"{URL_APP}/{endpoint}"
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    data ={
        "title": title,
        "body": body,
    }

    resp = requests.post(url, headers=headers, json=data)

    print(resp.status_code)
    print(resp.json())


@app.command()
def get_all_articles():
    print("All Articles")

    endpoint = "articles/list"
    url = f"{URL_APP}/{endpoint}"

    resp = requests.get(url)

    print(resp.status_code)
    print(resp.json())


@app.command()
def get_one_article(article_id:int):
    typer.echo(f"Article {article_id}")

    endpoint = "articles/list"
    url = f"{URL_APP}/{endpoint}/{article_id}"

    resp = requests.get(url)

    print(resp.status_code)
    print(resp.json())

@app.command()
def delete_one_article(article_id:int):
    typer.echo(f"Article {article_id} deleted")
    
    endpoint = "articles/delete"
    url = f"{URL_APP}/{endpoint}/{article_id}"

    headers = CaseInsensitiveDict()
    headers["accept"] = "*/*"


    resp = requests.delete(url, headers=headers)

    print(resp.status_code)

if __name__ == "__main__":
    app()