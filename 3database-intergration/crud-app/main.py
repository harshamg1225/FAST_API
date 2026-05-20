from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List
import schemas
import crud


# creating table that present in Base.metdata
Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency with the db
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# endpoint
# 1 . Create an employee


@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):

    return crud.create_employee(db=db, employee=employee)


# 2 . get an all employees


@app.get("/employees", response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db=db)


# 3 get single employee
@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):

    db_employee = crud.get_employee(db=db, emp_id=emp_id)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not exists in data base")
    return db_employee


# 4 update employees
@app.put("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(
    emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)
):

    db_employee = crud.update_employee(db=db, emp_id=emp_id, employee=employee)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="employee not exists")
    return db_employee


# 5 delete employee
@app.delete("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):

    db_employee = crud.delete_employee(db=db, emp_id=emp_id)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="employee not exists")
    return db_employee
