from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    address:str = None

#create new user api
@app.post("/create")
def create_user(user: User):
    print("Received user data:", user)
    return {"message": "User created successfully", "data": user}
