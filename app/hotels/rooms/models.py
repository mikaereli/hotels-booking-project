from app.database import Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship

class Rooms(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)

    hotel = relationship("Hotels", back_populates="room")
    booking = relationship("Bookings", back_populates="room")

    def __str__(self):
        return f"Rooms #{self.id}"