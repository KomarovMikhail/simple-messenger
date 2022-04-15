from auth_server import app
from auth_server.const.const import SERVER_HOST, SERVER_PORT

# controllers
from auth_server.controllers import login_controller
from auth_server.controllers import register_controller
from auth_server.controllers import delete_user_controller
from auth_server.controllers import refresh_tokens_controller
from auth_server.controllers import logout_controller


if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT)
