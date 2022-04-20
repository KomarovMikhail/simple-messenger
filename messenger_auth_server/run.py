from auth_server import app
from auth_server.const.const import SERVER_HOST, SERVER_PORT

# controllers
from auth_server.controllers import root_controller
from auth_server.controllers import login_controller
from auth_server.controllers import register_controller
from auth_server.controllers import delete_user_controller
from auth_server.controllers import refresh_tokens_controller
from auth_server.controllers import logout_controller
from auth_server.controllers import logs_controller
from auth_server.controllers import add_user_deleted_webhook_controller
from auth_server.controllers import remove_user_deleted_webhook_controller

# loggers
from auth_server.logging_utils.loggers import db_logger


if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT)
