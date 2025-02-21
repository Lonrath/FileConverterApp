import os

from fastapi import FastAPI
from routes.converter import router

# Temp klasörünü oluştur
os.makedirs("temp", exist_ok=True)

app = FastAPI()
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}
