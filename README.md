# fastapi_heroku_db

First create the database.py file

Import the SQLAlchemy parts:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
```


Create a database URL for SQLAlchemy:

The file will be located at the same directory in the file `sqlite:///./STUDENT.db`.
```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./STUDENT.db"
```

Create the SQLAlchemy engine:
The first step is to create a SQLAlchemy "engine".

We will later use this engine in other places.
```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
```
