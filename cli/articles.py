import typer

app = typer.Typer()

@app.command()
def create_article(title:str, body:str):
    print(f"title : {title}")
    print(f"body : {body}")

@app.command()
def get_all_articles():
    print("All Articles")

@app.command()
def get_one_article(article_id:int):
    print(f"Article {article_id}")

@app.command()
def delete_one_article(article_id:int):
    print(f"Article {article_id} deleted")

if __name__ == "__main__":
    app()