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
            USER (JSON) : name, id, pwd, user_id  
    <br>

    - **_/users/connect_** : to connect to the blog platform  
        - POST method   
        - ARGS :  
            USER.id  
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