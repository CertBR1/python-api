from src.services.auth_service import auth_service

class auth_controller:
    @staticmethod
    def login_controller():
        print("Login Controller")
        return auth_service.login()
    
    @staticmethod
    def register_controller(username: str, password: str):
        print("register Controller")
        return auth_service.register(username, password)

auth_controller = auth_controller()