from sqladmin import ModelView

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.users.models import Users

class UsersView(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    can_edit = False
    name = "Пользователь"
    name_plural = "Пользователи"

class BookingView(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.columns] + [Bookings.user, Bookings.room]
    can_delete = True
    name = "Брони"
    name_plural = "Бронирования"

class RoomsView(ModelView, model=Rooms):
    column_list = [c.name for c in Rooms.__table__.columns] + [Rooms.hotel, Rooms.booking]
    name = "Комнаты"
    name_plural = "Комнаты"


class HotelsView(ModelView, model=Hotels):
    column_list = [c.name for c in Hotels.__table__.columns] + [Hotels.room]
    name = "Отели"
    name_plural = "Отели"