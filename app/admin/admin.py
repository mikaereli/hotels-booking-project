from app.main import app
from sqladmin import Admin
from app.admin.views import BookingView, HotelsView, RoomsView, UsersView
from app.admin.auth import authentication_backend
from app.database import engine


admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersView)
admin.add_view(BookingView)
admin.add_view(HotelsView)
admin.add_view(RoomsView)