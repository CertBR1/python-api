from flask import Blueprint
from flask import request
from src.controllers.auth_controller import auth_controller

class RouterDefault:
    bp = Blueprint("router_default", __name__)

    @bp.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        print("Login =>>>>>>>>>>>", data.get('username'))
        return auth_controller.login_controller()

    @bp.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        print("Register =>>>>>>>>>>>", username, password)
        return auth_controller.register_controller(username, password)

router_default = RouterDefault()