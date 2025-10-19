from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

contacts: list[dict] = []

class Contact(BaseModel):
    name: str
    phone: str

class ContactUpdate(BaseModel):
    phone: str

@router.get("/")
def home():
    return {"message": "Contacts API is running!"}

@router.get("/contacts")
def get_contacts():
    return contacts

@router.get("/contacts/{name}")
def get_contact(name: str):
    for c in contacts:
        if c["name"].lower() == name.lower():
            return c
    raise HTTPException(status_code=404, detail="Contact not found")

@router.post("/contacts", status_code=201)
def add_contact(contact: Contact):
    for c in contacts:
        if c["name"].lower() == contact.name.lower():
            raise HTTPException(status_code=409, detail="Contact already exists")
    contacts.append(contact.dict())
    return {"message": "Contact added", "contact": contact}

@router.delete("/contacts/{name}")
def delete_contact(name: str):
    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            return {"message": f"Contact {name} deleted"}
    raise HTTPException(status_code=404, detail="Contact not found")

@router.put("/contacts/{name}")
def update_contact(name: str, payload: ContactUpdate):
    for c in contacts:
        if c["name"].lower() == name.lower():
            c["phone"] = payload.phone
            return {"message": f"Contact {name} updated", "contact": c}
    raise HTTPException(status_code=404, detail="Contact not found")

@router.patch("/contacts/{name}")
def patch_contact(name: str, payload: ContactUpdate):
    for c in contacts:
        if c["name"].lower() == name.lower():
            if payload.phone:
                c["phone"] = payload.phone
            return {"message": f"Contact {name} patched", "contact": c}
    raise HTTPException(status_code=404, detail="Contact not found")
