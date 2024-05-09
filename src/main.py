from flask import Flask
from src.routes.router_default import router_default
from src.database.database_client import init_db

app = Flask(__name__)
init_db()
app.register_blueprint(router_default.bp)