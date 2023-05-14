from api_config import get_api

app = get_api()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
