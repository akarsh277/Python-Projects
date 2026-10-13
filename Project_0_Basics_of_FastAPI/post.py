from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

class Product(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=10, le=100000)#field validation for price, must be greater than 10 and less than or equal to 100000
    quantity: int = Field(ge=0, le=1000)
    in_stock: bool=True

@app.post("/products")
def create_product(product: Product):
    total_value = product.price * product.quantity
    return {"message": "Product created",
            "product": product,
            "total value": total_value
        }
