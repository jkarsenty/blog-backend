# blog-backend

### Backend of a blog with python as an API.  
### A CLI will be available to test the API.   
#

### **API Documentation**

**To visualize the API documentation go to : http://127.0.0.1:8000/docs**

**The API will contain those functions (for now) :**   
- create users.
- users connection.
- create articles.
- get articles.

<br>

**API Endpoints :**

- **_/login_** : to login to the blog platform  
    - POST method   
    - ARGS :  
        LOGIN.username  
        LOGIN.pwd  
    <br>

- **_/users_**  : All actions about the users  
  
    - **_/users/create_** : to create a new user  
        - POST method  
        - ARGS :  
            USER (JSON) : user_id, name, login, pwd  
    <br>

    - **_/users/list_** : to list all users  
        - GET method  
    <br>

    - **_/users/list/{user_id}_** : to get user of id {user_id}  
        - GET method  
        - ARGS :  
            user_id (int)  
    <br>

    - **_/users/delete/{user_id}_** : to delete user of id {user_id}  
        - DELETE method  
        - ARGS :  
            user_id (int)  
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

    - **_/articles/list/{article_id}_** : to get article of id {article_id}  
        - GET method  
        - ARGS :  
            article_id (int)  
    <br>

    - **_/articles/delete/{article_id}_** : to delete article of id {article_id}  
        - DELETE method  
        - ARGS :  
            article_id (int)
    <br>

### **Data Schemas :**

- User :  
    - user_id : str  
    - name : str  
    - login : str  
    - pwd : str  
<br>

- Article :  
    - article_id : str  
    - title : str  
    - body : str  
<br>

- Login :  
    - username : str  
    - pwd : str  
