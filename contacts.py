from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# دیتابیس ساده در حافظه
contacts: list[dict] = []

class Contact(BaseModel):
    name: str
    phone: str

class ContactUpdate(BaseModel):
    phone: str  # برای PUT/PATCH

@app.get("/")
def home():
    return {"message": "Contacts API is running!"}

@app.get("/contacts")
def get_contacts():
    return contacts

@app.get("/contacts/{name}")
def get_contact(name: str):
    for c in contacts:
        if c["name"].lower() == name.lower():
            return c
    raise HTTPException(status_code=404, detail="Contact not found")

@app.post("/contacts", status_code=201)
def add_contact(contact: Contact):
    # جلوگیری از نام تکراری
    for c in contacts:
        if c["name"].lower() == contact.name.lower():
            raise HTTPException(status_code=409, detail="Contact already exists")
    contacts.append(contact.dict())
    return {"message": "Contact added", "contact": contact}

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    for c in contacts:
        if c["name"].lower() == name.lower():
            contacts.remove(c)
            return {"message": f"Contact {name} deleted"}
    raise HTTPException(status_code=404, detail="Contact not found")

# --- جدیدها ---

# PUT: آپدیت کاملِ فیلدهای قابل ویرایش (فعلاً فقط phone)
@app.put("/contacts/{name}")
def update_contact(name: str, payload: ContactUpdate):
    for c in contacts:
        if c["name"].lower() == name.lower():
            c["phone"] = payload.phone
            return {"message": f"Contact {name} updated", "contact": c}
    raise HTTPException(status_code=404, detail="Contact not found")

# PATCH: آپدیت جزیی (الزامی نیست ولی خوبه داشته باشیم)
@app.patch("/contacts/{name}")
def patch_contact(name: str, payload: ContactUpdate):
    for c in contacts:
        if c["name"].lower() == name.lower():
            # در آینده اگر فیلدهای بیشتری داشتیم، اینجا شرطی آپدیت می‌کنیم
            if payload.phone:
                c["phone"] = payload.phone
            return {"message": f"Contact {name} patched", "contact": c}
    raise HTTPException(status_code=404, detail="Contact not found")
