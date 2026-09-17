from pydantic import BaseModel, Field, EmailStr


class Employee(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    age: int = Field(gt=18, lt=65)
    department: str = Field(min_length=2, max_length=30)
    role: str = Field(min_length=2, max_length=30)
    salary: int = Field(gt=10000)
    email: EmailStr


class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    role: str
    email: EmailStr
    salary: int
