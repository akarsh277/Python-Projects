from fastapi import FastAPI
from pydantic import BaseModel,EmailStr,Field,field_validator
app = FastAPI()

class Address(BaseModel):
    city:str
    state:str
    country:str

class EmployeeCreate(BaseModel):
    name:str=Field(min_length=3,max_length=30)
    email:EmailStr
    age:int=Field(ge=21,le=60)
    salary:int=Field(gt=20000)
    address:Address
    department:str
    @field_validator("department")
    @classmethod
    def validate(cls, value):
        if value.lower().startswith("test"):
            raise ValueError("Department name can't be test")
        return value
    @field_validator("department")
    @classmethod
    def validate_dept(cls, value):
        if value.lower() not in ["it","hr","finance","marketing"]:
            raise ValueError("Department must be IT, HR, Finance or Marketing")
        return value
    
class EmployeeResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    department:str
    address:Address

@app.post("/employees",response_model=EmployeeResponse)
def create_employee(id:int, employee:EmployeeCreate):
    return{
        "id":id,
        "name":employee.name,
        "email":employee.email,
        "department":employee.department,
        "address":employee.address
    }

@app.get("/employees",response_model=list[EmployeeResponse])
def get_employees():
    return[
        {
            "id": 101,
            "name": "Ravi",
            "email": "ravi@gmail.com",
            "department": "IT",
            "address": {
                "city": "Hyderabad",
                "state": "Telangana",
                "country": "India",
            }
        },
        {
            "id": 102,
            "name": "Akarsh",
            "email": "akarsh@gmail.com",
            "department": "HR",
            "address": {
                "city": "Vijayawada",
                "state": "Andhra Pradesh",
                "country": "India",
            }
        },
        {
            "id": 103,
            "name": "Rahul",
            "email": "rahul@gmail.com",
            "department": "Finance",
            "address": {
                "city": "Chennai",
                "state": "Tamil Nadu",
                "country": "India",
            }
        },
        {
            "id": 104,
            "name": "Kiran",
            "email": "kiran@gmail.com",
            "department": "Marketing",
            "address": {
                "city": "Bengaluru",
                "state": "Karnataka",
                "country": "India",
            }
        }
    ]

@app.get("/employee",response_model=EmployeeResponse)
def get_employee():
    return{
        "id": 101,
        "name": "Ravi",
        "email": "ravi@gmail.com",
        "department": "IT",
        "address": {
            "city": "Hyderabad",
            "state": "Telangana",
            "country": "India",
        }  
    }