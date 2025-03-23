from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database.db import SessionLocal, engine, Base
from scraper.models import OutletDB
from typing import List
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)
app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for serialization
class OutletResponse(BaseModel):
    id: int
    name: str
    address: str
    phone: str
    latitude: float
    longitude: float
    features: str
    waze_link: str

    class Config:
        orm_mode = True

@app.get("/outlets", response_model=List[OutletResponse])
def read_outlets(db: Session = Depends(get_db)):
    return db.query(OutletDB).all()