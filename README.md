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

Import the SQLAlchemy parts:

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



