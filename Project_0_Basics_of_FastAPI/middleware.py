from fastapi import FastAPI, Request
app = FastAPI()

@app.middleware("http")
async def mw(request: Request, call_next):
    print("request started")
    response = await call_next(request)
    print("request finished")
    return response

@app.get("/")
def home():
    print("Inside Home")
    return {"message": "Hello"}