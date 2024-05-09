import src.database.database_client as db
from src.database.models.user_entity import UserEntity
from argon2 import PasswordHasher
from flask_api import status
passwordHasher = PasswordHasher()
class AuthService:
    @staticmethod
    def login(username: str, password: str):
        user = db.UserEntity.select().where(db.UserEntity.username == username).first()
        if user is None:
            return {'message': 'User not found'}, status.HTTP_404_NOT_FOUND
        if not passwordHasher.verify(user.password, password):
            return {'message': 'Incorrect password'}, status.HTTP_401_UNAUTHORIZED
        return {'id': user.id, 'username': user.username}
    @staticmethod
    def register(username: str, password: str):
        with db.orm.db_session:
            hashed_password = passwordHasher.hash(password)
            newuser = UserEntity(username=username, password=hashed_password)
            db.orm.commit()
            return {'id': newuser.id, 'username': newuser.username}

auth_service = AuthService()