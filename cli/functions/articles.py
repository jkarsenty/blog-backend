import typer
import requests
from requests.structures import CaseInsensitiveDict

URL_APP = "http://www.localhost:8000"

#app_articles = typer.Typer()

#@app_articles.command()
def create_article(title:str, body:str):
    typer.echo("Creating Article ...")
    typer.echo(f"title : {title}")
    typer.echo(f"body : {body}")

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

    typer.echo(resp.status_code)
    typer.echo(resp.json())
    typer.echo("Article Created")

#@app_articles.command()
def get_all_articles():
    typer.echo("Getting all articles ...")

    endpoint = "articles/list"
    url = f"{URL_APP}/{endpoint}"
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    typer.echo(resp.status_code)
    typer.echo(resp.json())


#@app_articles.command()
def get_one_article(article_id:int):
    typer.echo(f"Getting article {article_id} ...")

    endpoint = "articles/list"
    url = f"{URL_APP}/{endpoint}/{article_id}"
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    typer.echo(resp.status_code)
    if resp.status_code == 200 :
        typer.echo(resp.json())
    else :
        typer.echo(f'Article of id {article_id} does not exist')

#@app_articles.command()
def delete_one_article(article_id:int):
    typer.echo(f"Deletting article {article_id} ...")
    
    endpoint = "articles/delete"
    url = f"{URL_APP}/{endpoint}/{article_id}"

    headers = CaseInsensitiveDict()
    headers["accept"] = "*/*"


    resp = requests.delete(url, headers=headers)

    typer.echo(resp.status_code)
    if resp.status_code == 404 :
        typer.echo(f'Article of id {article_id} does not exist')
    elif resp.status_code == 204 :
        typer.echo(f"Article of id {article_id} deleted")

# if __name__ == "__main__":
#     app_articles()