import typer

app = typer.Typer()

@app.command()
def login(username:str, pwd:str):
    print(f"username : {username}")
    print(f"password : {pwd}")

if __name__ == "__main__":
    app()