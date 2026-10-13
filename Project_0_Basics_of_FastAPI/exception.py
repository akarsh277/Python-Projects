from fastapi import FastAPI, HTTPException
app = FastAPI()

products = {
    1: "Laptop",
    2: "Keyboard",
    3: "Mouse"
}
@app.get("/products/{id}")
def get_p(id:int):
    if id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return{"id": id, "name": products[id]}