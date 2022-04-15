from auth_server import app
from auth_server.const.const import REGISTER_URL, JSON_KEY_LOGIN, JSON_KEY_PASSWORD
from auth_server.const.http_codes import RESPONSE_CODE_BAD_REQUEST
from auth_server.const.error_messages import ERROR_MESSAGE_INVALID_REQUEST_BODY
from auth_server.jwt_utils.jwt_handler import JwtHandler

from flask import request
from flask import Response


@app.route(REGISTER_URL, methods=['POST'])
def register_controller():
    request_body = request.json
    if JSON_KEY_LOGIN not in request_body or JSON_KEY_PASSWORD not in request_body:
        return Response(response=ERROR_MESSAGE_INVALID_REQUEST_BODY, status=RESPONSE_CODE_BAD_REQUEST)

    login = request_body[JSON_KEY_LOGIN]
    password = request_body[JSON_KEY_PASSWORD]

    return JwtHandler.register(login, password)
