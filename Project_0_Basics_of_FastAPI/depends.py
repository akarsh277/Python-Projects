from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    print("Database Connected")
    return "DB Connection"

@app.get("/students")
def get_students(db=Depends(get_db)):
    return {"db": db}

@app.get("/teachers")
def get_teachers(db=Depends(get_db)):
    return {"db": db}

@app.get("/courses")
def get_courses(db=Depends(get_db)):
    return {"db": db}