from fastapi import HTTPException
from data import students

def find_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            return index, student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )