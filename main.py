from fastapi import FastAPI
from contacts import router as contacts_router

app = FastAPI()
app.include_router(contacts_router)
