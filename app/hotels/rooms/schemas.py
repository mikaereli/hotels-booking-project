from typing import List, Optional
from pydantic import BaseModel, Json

class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    services: List[str]
    price: int
    quantity: int
    image_id: int

    class Config:
        orm_mode = True


class SRoomsInfo(SRooms):
    total_cost: int
    rooms_left: int

    class Config:
        orm_mode = True