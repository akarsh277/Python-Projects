from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{id}/users/{name}")
def get_item(id:int, name:str):
    return {"id": id, "name": name}

@app.get("/students/{course}")
def get_students(course:str, limit:int):#limit is a query parameter
    return {"course": course, "limit": limit}