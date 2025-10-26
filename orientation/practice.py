from fastapi import FastAPI

app = FastAPI()

#Phone numbers
# Dictionary of people who's names and phone number received
phone_numbers = {
    # Name: Phone Number
}


"""
GET ENDPOINTS
"""

@app.get("/")
def root_endpoint():
    """
    TODO:
    - Return a simple JSON message confirming the server is running.
    - Example response: {"message": "Server is live!"}
    """
    return {"message": "Server is live!"}, 200

@app.get("/hello/{name}")
def greet_user(name: str):
    """
    TODO:
    - Accept a name from the path.
    - Return a JSON greeting that includes the name.
    - Example: GET /hello/Morgan → {"message": "Hello Morgan!"}
    """
    pass

@app.get("/phone_numbers/")
def get_phone_number():
    """
    TODO:
    - Accept a name from the path.
    - Return the phone number for the given name.
    - Example: GET /phone_numbers/Morgan → {"phone_number": "123-456-7890"}
    """
    pass


"""
POST ENDPOINTS
"""

@app.post("/echo/")
def echo_message(payload: dict):
    """
    TODO:
    - Accept any JSON object in the body.
    - Return the same object in a field called 'you_sent'.
    - Example: {"you_sent": {"foo": "bar"}}
    """
    pass

# CREATE A POST REQUEST that adds a new phone number to the dictionary and returns the updated dictionary

#@app.post...