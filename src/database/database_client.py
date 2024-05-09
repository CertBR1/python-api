from pony import orm

db = orm.Database()
def init_db():
    db.bind(provider="sqlite", filename="database.db", create_db=True)
    db.generate_mapping(create_tables=True)

__all_ = ["db", "init_db"]
