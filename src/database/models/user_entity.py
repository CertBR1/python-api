from pony import orm
from src.database.database_client import db

class UserEntity(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    username = orm.Required(str)
    password = orm.Required(str)