# fastapi_heroku_db

### First create the database.py file

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

The first step is to create a SQLAlchemy `engine`.
We will later use this engine in other places.

```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
```

Create a dependency:
We need to have an independent database session/connection (SessionLocal) per request, use the same session through all the request and then close it after the request is finished.






Create a SessionLocal class: 

Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.

But once we create an instance of the SessionLocal class, this instance will be the actual database session.
```python
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```





Create a Base class: 

Later we will inherit from this class to create each of the database models or classes
```python
Base = declarative_base()
```



### Then I create the models.py file:

Import the parts:

```python 
from sqlalchemy import Column, Integer, String
from database import Base
```


Create tables:

```python
class Students(Base):
    __tablename__ = "students"

    name = Column(String, primary_key=True, index=True)
    tarikh = Column(Integer)
    zaban = Column(Integer)
```


### Then I create the main.py file:

We integrate and use all the other parts we created earlier.
Import the parts:

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
```


Build app:
```python
app = FastAPI()
```
Create the database tables:
```python
models.Base.metadata.create_all(bind=engine)
```


Create a dependency:

We need to have an independent database session/connection (`SessionLocal`) per request, use the same session through all the request and then close it after the request is finished.

```python

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
```


We create a class that inherits from BaseModel:
```python
class Student(BaseModel):
    name: str 
    tarikh: int 
    zaban: int 
```

Using the get method, we read the data, 
we are creating the database session before each request in the dependency with yield, and then closing it afterwards.
```python
@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Students).all()
```




