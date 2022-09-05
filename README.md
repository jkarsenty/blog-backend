# blog-backend

### blog : Backend of a blog with python as an API.
### cli : A CLI will be available to test the API.
<br>

## Blog 

To Build the backend of the blog :  
```sh
docker build ./blog -t blog-backend
```

To Run it :
```sh
docker run -p 8000:8000 blog-backend
```
<br>

## CLI 

To Build the backend of the blog :  
```sh
docker build ./cli -t blog-cli
```

To Run it :
```sh
docker run blog-cli
```
