from app.database import Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Date, Boolean

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)