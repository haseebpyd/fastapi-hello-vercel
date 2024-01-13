from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Welcome!"

@app.get("/hi/{who}")
def greet(who:str):
    return f"Hello? {who}?"

# @app.get("/hi/{who}/piaic")
# def greet(who:str):f
#     return f"Hello? {who}?"