from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()

class ProductCreate(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)

class ProductResponse(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)

@app.post("/products", response_model=ProductResponse)
def create(product:ProductCreate):
    return product
