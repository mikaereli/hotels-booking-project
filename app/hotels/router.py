import asyncio
from datetime import date, datetime, timedelta
import json
from typing import List
from fastapi import APIRouter, HTTPException, Query
from app.hotels.dao import HotelDao
from app.hotels.models import Hotels
from app.hotels.schemas import SHotels
from fastapi_cache.decorator import cache
from pydantic import TypeAdapter
router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)

@router.get("/{location}")
@cache(expire=30)
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
)  -> List[SHotels]:
    if date_from > date_to:
        raise HTTPException(status_code=400, detail="Дата начала бронирования не может быть позже даты окончания")
    if (date_to - date_from).days > 31:
        raise HTTPException(status_code=400, detail="Максимальное количество дней бронирования - 31")
    await asyncio.sleep(3)
    hotels = await HotelDao.find_all(location, date_from, date_to)
    hotels_dict = [
    {**dict(row._mapping), "services": json.dumps(row.services)}
    for row in hotels
    ]
    return TypeAdapter(List[SHotels]).validate_python(hotels_dict)

    
