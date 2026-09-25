from fastapi import FastAPI

app = FastAPI()

#home page
@app.get("/")
def home():
    return {"message": "Hello, World! this is my home page."}

#get all users
@app.get("/users")
def get_users():
    return {"users": [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]}

#Get specific user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "message": f"User with ID {user_id} retrieved successfully."}
