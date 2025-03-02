from pydantic import BaseModel, Json

class SHotels(BaseModel):
    id: int
    name: str
    location: str 
    services: Json
    rooms_quantity: int
    image_id: int

    class Config:
        orm_mode = True