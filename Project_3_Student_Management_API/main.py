from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from data import students
from schemas import Student, StudentResponse
from dependencies import find_student
from middleware import log_requests
from tasks import send_welcome_email, create_student_report
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
    return {"message": "Welcome to Student Management API"}


@app.post("/students", response_model=StudentResponse)
def create_student(student: Student, background_tasks: BackgroundTasks):
    student_data = student.model_dump()

    if students:
        student_data["id"] = students[-1]["id"] + 1
    else:
        student_data["id"] = 1

    students.append(student_data)

    background_tasks.add_task(send_welcome_email, student_data["name"])

    background_tasks.add_task(create_student_report, student_data["name"])

    return student_data


@app.get("/students", response_model=list[StudentResponse])
def get_students():
    return students


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(result=Depends(find_student)):
    index,student=result
    return student


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(updated_student: Student, result=Depends(find_student)):
    index, student = result

    student_data = updated_student.model_dump()
    student_data["id"] = student["id"]

    students[index] = student_data

    return student_data


@app.delete("/students/{student_id}")
def delete_student(result=Depends(find_student)):
    index, student = result

    students.pop(index)

    return {"message": "Student deleted successfully"}
