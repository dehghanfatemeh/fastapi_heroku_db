from sqlalchemy import Column, Integer, String
from database import Base


class Students(Base):
    __tablename__ = "students"

    name = Column(String, primary_key=True, index=True)
    tarikh = Column(Integer)
    zaban = Column(Integer)
 