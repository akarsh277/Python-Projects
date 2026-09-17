from pydantic import BaseModel, Field, EmailStr

class Student(BaseModel):
    name:str=Field(min_length=3,max_length=30)
    age:int=Field(gt=17,lt=60)
    department:str=Field(min_length=2,max_length=20)
    email:EmailStr

class StudentResponse(BaseModel):
    id:int
    name:str
    department:str
    email:EmailStr