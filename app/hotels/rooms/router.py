from datetime import date, datetime, timedelta
from typing import List
from fastapi import Query
from app.hotels.rooms.dao import RoomsDao
from app.hotels.rooms.schemas import SRoomsInfo
from app.hotels.router import router 

@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int, 
              date_from: date = Query(..., description=f"Например, {datetime.now().date()}"), 
              date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}")) -> List[SRoomsInfo]:
    rooms = await RoomsDao.find_all(hotel_id, date_from, date_to)
    return rooms    

    