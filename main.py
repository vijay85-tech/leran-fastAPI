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

#Get specific user by ID(path parameter)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "message": f"User with ID {user_id} retrieved successfully."}

#query parameter
#search users by name(required params)
@app.get("/search")
def search_users(q: str):
    return {"query": q, "message": f"Searching for users with query '{q}'."}

#query parameter with optional params
@app.get("/filter-data")
def filter_data(min_age: int = None, max_age: int = None):
    if min_age is None or max_age is None:
        return {"message": "No age filters provided."}
    return {"min_age": min_age, "max_age": max_age, "message": "Filtering data based on age."}
