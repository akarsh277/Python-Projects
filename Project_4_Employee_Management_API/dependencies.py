from fastapi import HTTPException
from data import employees


def find_employee(employee_id: int):
    for index, employee in enumerate(employees):
        if employee["id"] == employee_id:
            return index, employee

    raise HTTPException(status_code=404, detail="Employee not found")
