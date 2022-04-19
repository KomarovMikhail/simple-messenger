from auth_server import app
from auth_server.const.const import LOGIN_URL, JSON_KEY_LOGIN, JSON_KEY_PASSWORD, JSON_KEY_FINGERPRINT
from auth_server.const.http_codes import RESPONSE_CODE_BAD_REQUEST
from auth_server.const.error_messages import ERROR_MESSAGE_INVALID_REQUEST_BODY
from auth_server.jwt_utils.jwt_handler import JwtHandler

from flask import request
from flask import Response


@app.route(LOGIN_URL, methods=['POST'])
def login_controller():
    request_body = request.json
    if JSON_KEY_LOGIN not in request_body or JSON_KEY_PASSWORD not in request_body or \
            JSON_KEY_FINGERPRINT not in request_body:
        return Response(status=RESPONSE_CODE_BAD_REQUEST, response=ERROR_MESSAGE_INVALID_REQUEST_BODY)

    login = request_body[JSON_KEY_LOGIN]
    password = request_body[JSON_KEY_PASSWORD]
    fingerprint = request_body[JSON_KEY_FINGERPRINT]

    return JwtHandler.login(login, password, fingerprint)
