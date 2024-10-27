# repositories/user_repository.py

from models import User
from app import db

class UserRepository:
    def get_user(self, user_id):
        return User.query.get(user_id)
    #usuarios por su id
    def get_all_users(self):
        return User.query.all()
    #todos los usuarios 
    def create_user(self, username, password_hash, is_admin=False):
        new_user = User(username=username, password_hash=password_hash, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    #creacion del usuario
    def update_user(self, user_id, username=None, password_hash=None, is_admin=None):
        user = User.query.get(user_id)
        if not user:
            return None
        if username is not None:
            user.username = username
        if password_hash is not None:
            user.password_hash = password_hash
        if is_admin is not None:
            user.is_admin = is_admin
        db.session.commit()
        return user
    #actualizar usuario
    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        db.session.delete(user)
        db.session.commit()
        return True
    #borrar usuario