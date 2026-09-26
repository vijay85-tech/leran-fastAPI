from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    name: str
    age: int

@app.post("/create-user/")
def create_user(user: User):
    return {"message": "User created successfully", "data": user}

#nested schema example
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class UserWithAddress(BaseModel):
    username: str
    email: str
    name: str
    age: int
    address: Address

@app.post("/create-user-with-address/")
def create_user_with_address(user_with_address: UserWithAddress):
    return {"message": "User with address created successfully", "data": user_with_address}