from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def test():
    return {"Test", "test"}