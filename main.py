from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Student(BaseModel):
    name: str 
    tarikh: int 
    zaban: int 


@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Students).all()

# ====================================================
@app.get("/average")
def average(db: Session = Depends(get_db)):

    avg = db.execute('SELECT name, (tarikh+ zaban )/2 as average FROM students').fetchall()


    return avg
# ======================================================================
@app.post("/insert")
def create(name: Student, db: Session = Depends(get_db)):

    student_model = db.query(models.Students).filter(models.Students.name == name.name).first()

    if student_model is None:
        student_model = models.Students(
          name = name.name,
          tarikh = name.tarikh,
          zaban = name.zaban
        )

    else:
        raise HTTPException(
            status_code=400,
            detail=f"name {name.name} : Does exist"
        )

    db.add(student_model)
    db.commit()

    return name
# ========================================================================
@app.put("/update/{name}")
def update(name: str, db: Session = Depends(get_db)):

    student_model = db.query(models.Students).filter(models.Students.name == name).first()

    if student_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"name {name} : Does not exist"
        )

    student_model.tarikh = student_model.tarikh + 1
    student_model.zaban = student_model.zaban + 1
  
    db.add(student_model)
    db.commit()

    return db.query(models.Students).filter(models.Students.name == name).first()
# =========================================================================

@app.delete("/{name}")
def delete(name: str, db: Session = Depends(get_db)):

    student_model = db.query(models.Students).filter(models.Students.name == name).first()

    if student_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"name {name} : Does not exist"
        )

    db.delete(student_model)

    db.commit()
    return 'ok'