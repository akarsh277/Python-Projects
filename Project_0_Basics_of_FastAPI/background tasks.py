from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def invoice():
    print("Invoice Generated")
def send_email():
    print("Confirmation Email Sent")


@app.post("/order")
def register(background_tasks: BackgroundTasks):

    background_tasks.add_task(invoice)
    background_tasks.add_task(send_email)

    return {
        "message": "Order placed successfully"
    }