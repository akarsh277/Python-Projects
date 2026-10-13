from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/about")
def about():
    return {"company": "ABC Tech"}

@app.get("/services")
def services():
    return {"services": ["Backend", "Frontend", "AI"]}

@app.get("/contact")
def contact():
    return { "email": "contact@abctech.com"}