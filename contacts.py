from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

contacts = []

class Contact(BaseModel):
    name: str
    phone: str


@app.get("/")
def home():
    return {"message": "Contacts API is running!"}


@app.get("/contacts")
def get_contacts():
    return contacts


@app.post("/contacts")
def add_contact(contact: Contact):
    contacts.append(contact.dict())
    return {"message": "Contact added", "contact": contact}


@app.get("/contacts/{name}")
def search_contact(name: str):
    for c in contacts:
        if c["name"].lower() == name.lower():
            return c
    return {"error": "Contact not found"}


@app.delete("/contacts/{name}")
def delete_contact(name: str):
    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            return {"message": f"Contact {name} deleted"}
    return {"error": "Contact not found"}
