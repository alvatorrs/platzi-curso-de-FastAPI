# Python
from typing import Optional
# Pydantic
from pydantic import BaseModel
# FastAPI
from fastapi import FastAPI
from fastapi import Body


app = FastAPI()


class Person(BaseModel):
    name: str
    last_name: str
    age: str
    marital_status: Optional[bool] = None



@app.get("/")
def home():
    return {'Mensaje': 'Hola, mundo!'}


# Request and Response Body

@app.post("/person/new") #
def create_person(person: Person = Body(...)):
    return person
