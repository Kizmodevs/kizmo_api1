from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Student (BaseModel):
    id : int
    name : str
    grade : float

students= [
    Student (id=1,name="Hakim zarouali",grade=13.2),
    Student (id=2,name="meriem bouchane",grade=18)
]

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student:Student):
   students.append(new_student)
   return new_student

@app.put("/student/{id_student}")
def update_student(id_student:int, updated_student:Student ):
    for index , Student in enumerate(students):
        if Student.id == id_student:
            students[index]=updated_student
            return updated_student
    return {"error":"student not found"}

@app.delete("/student/{id_student}")
def delete_student(id_student: int):
    for index, Student in enumerate(students):
        if Student.id==id_student:
            del students[index]
            return {"Message":"Student deleted"}
    return {"error":"student not found"}


