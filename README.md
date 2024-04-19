# simple-django-blog-app

### First create an env with

```
python3 -m venv .venv
source ./.venv/bin/activate
```

### Then, install all dependencies

```
pip install -r requirements.txt
```

### Run the migrations

```
./manage.py migrate
```

### Finally, run the project

```
./manage.py runserver
```

### GraphiQL can be access through

```
http://127.0.0.1:8000/graphql/
```

```
mutation CreatePost($text: String!) {
  createPost(text: $text){
    post {
      text
    }
  }
}
```

```
{
  "text": "this is a test post"
}
```
