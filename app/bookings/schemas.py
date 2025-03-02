from datetime import date
from pydantic import BaseModel, Json

class SBooking(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        orm_mode = True

class SBookingInfo(SBooking):
    image_id: int
    name: str
    description: str
    sercises: Json

    class Config: 
        orm_mod = True
