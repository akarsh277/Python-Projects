from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from data import employees
from schemas import Employee, EmployeeResponse
from dependencies import find_employee
from middleware import log_requests
from tasks import send_onboarding_email, create_payroll_record
from exceptions import http_exception_handler

app = FastAPI()

# Register Middleware
app.middleware("http")(log_requests)

# Register Custom Exception Handler
app.add_exception_handler(HTTPException, http_exception_handler)

# Register CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Welcome to Employee Management API"}


@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: Employee, background_tasks: BackgroundTasks):
    employee_data = employee.model_dump()

    if employees:
        employee_data["id"] = employees[-1]["id"] + 1
    else:
        employee_data["id"] = 1

    employees.append(employee_data)

    background_tasks.add_task(send_onboarding_email, employee_data["name"])
    background_tasks.add_task(create_payroll_record, employee_data["name"])

    return employee_data


@app.get("/employees", response_model=list[EmployeeResponse])
def get_employees():
    return employees


@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(result=Depends(find_employee)):
    index, employee = result
    return employee


@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(updated_employee: Employee, result=Depends(find_employee)):
    index, employee = result

    employee_data = updated_employee.model_dump()
    employee_data["id"] = employee["id"]

    employees[index] = employee_data

    return employee_data


@app.delete("/employees/{employee_id}")
def delete_employee(result=Depends(find_employee)):
    index, employee = result

    employees.pop(index)

    return {"message": "Employee deleted successfully"}
