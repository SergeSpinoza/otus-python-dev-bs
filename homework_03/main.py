from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ping/", status_code=200)
def ping():
    return {
        "message": "pong"
    }
