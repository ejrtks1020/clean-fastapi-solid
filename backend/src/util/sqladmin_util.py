from sqladmin import Admin, ModelView
from model.user.user_model import User
from fastapi import FastAPI
from db.session import engine

class UserAdmin(ModelView, model=User):
    column_list = [
      User.id, 
      User.email,
      User.password,
      User.first_name,
      User.last_name
    ]

def set_admin(app: FastAPI):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)