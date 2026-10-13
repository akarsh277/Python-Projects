from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, field_validator
app = FastAPI()


class Address(BaseModel):
    city: str
    state: str

class StudentCreate(BaseModel):
    name: str = Field(min_length=3, max_length=30)

    @field_validator("name")
    @classmethod
    def validate_name(cls,value):
        if value.lower().startswith("test"):
            raise ValueError("Name should not start with test")
        return value
    
    email: EmailStr
    age: int = Field(ge=18, le=30)
    marks: float = Field(ge=0, le=100)
    address: Address

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Address


@app.post("/students", response_model=StudentResponse)
def create_students(id:int, student:StudentCreate):
    return {
        "id": id,
        "name": student.name,
        "email": student.email,
        "address": student.address,
    }

@app.get("/students", response_model=list[StudentResponse])
def get_students():
    return [
        {
            "id": 1,
            "name": "Akarsh",
            "email": "akarsh@gmail.com",
            "address": {
                "city": "Hyderabad",
                "state": "Telangana"
            }
        },
        {
            "id": 2,
            "name": "Rahul",
            "email": "rahul@gmail.com",
            "address": {
                "city": "Vijayawada",
                "state": "Andhra Pradesh"
            }
        },
        {
            "id": 3,
            "name": "Kiran",
            "email": "kiran@gmail.com",
            "address": {
                "city": "Visakhapatnam",
                "state": "Andhra Pradesh"
            }
        }
    ]

@app.get("/student", response_model=StudentResponse)
def get_student():
    return {
        "id": 1,
        "name": "Akarsh",
        "email": "akarsh@gmail.com",
        "address": {
            "city": "Hyderabad",
            "state": "Telangana"
        }
    }