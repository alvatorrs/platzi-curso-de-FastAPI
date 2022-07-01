# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI(title="Request and response body")

# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: str
    is_married: Optional[bool] = None


@app.get("/")
def home():
    return {'Mensaje': 'Hola, mundo!'}


# Request and Response Body

@app.post("/person/new") #request body
def create_person(person: Person = Body(...)):
    return person
