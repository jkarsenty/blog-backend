import typer

app = typer.Typer()

@app.command()
def create_user(name:str, login:str, pwd:str):
    print(f"name : {name}")
    print(f"login : {login}")
    print(f"pwd : {pwd}")

@app.command()
def get_all_users():
    print("All Users")

@app.command()
def get_one_user(user_id:int):
    print(f"User {user_id}")

@app.command()
def delete_one_user(user_id:int):
    print(f"User {user_id} deleted")


if __name__ == "__main__":
    app()