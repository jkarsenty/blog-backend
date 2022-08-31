# blog-backend

### Backend of a blog with python as an API.  
### A CLI will be available to test the API.   
#
**The API will contain those functions (for now) :**   
- create users.
- users connection.
- create articles.
- get articles.

<br>

**API Documentation :**

- **_/users_**  : All actions about the users  
  
    - **_/users/list_** : to list all users  
        - GET method  
    <br>

    - **_/users/create_** : to create a new user  
        - POST method  
        - ARGS :  
            USER (JSON) : user_id, name, connect_id, pwd  
    <br>

    - **_/users/connect_** : to connect to the blog platform  
        - POST method   
        - ARGS :  
            USER.connect_id  
            USER.pwd  
<br>

- **_/articles_** : All actions about the articles  
  
    - **_/articles/create_** : to create a new article  
        - POST method  
        - ARGS :  
            ARTICLE (JSON) : title, body, article_id  
    <br>

    - **_/articles/list_** : to get the list of all articles  
        - GET method

<br>

**Data Tables :**

- User :  
    - user_id : str  
    - name : str  
    - connect_id : str  
    - pwd : str  
<br>

- Article :  
    - article_id : str  
    - title : str  
    - body : str  