from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom Exception Handler
@app.exception_handler(HTTPException)
async def custom_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail
        }
    )

# Endpoint
@app.get("/student/{id}")
def get_student(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": 1,
        "name": "Akarsh"
    }