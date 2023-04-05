# Blog with user
In this project a user with authentication can perform a crud of blog


### Clone project use follwing command
```
git clone https://github.com/ongraphpythondev/blogFastapi.git
```

### Create a virtual enviorment and activate it
```
python -m venv venv
source venv/bin/activate
```

### Install dependencies to run the project
```
pip install -r requirments.txt
```

### Run the project
```
uvicorn main:app --reload
```

### visit the following page to create and get the user
```
127.0.0.1:8000/user
127.0.0.1:8000/user/{id}
```
### After login you can get the blog 
### visit the following page to create, get, get all, update and delete a blog
```
127.0.0.1:8000/blog
127.0.0.1:8000/blog/{id}
```
