from auth_server import app
from auth_server.const.const import LOGOUT_URL, JSON_KEY_LOGIN, JSON_KEY_FINGERPRINT
from auth_server.const.http_codes import RESPONSE_CODE_BAD_REQUEST
from auth_server.const.error_messages import ERROR_MESSAGE_INVALID_REQUEST_BODY
from auth_server.jwt_utils.jwt_handler import JwtHandler

from flask import request
from flask import Response


@app.route(LOGOUT_URL, methods=['POST'])
def logout_controller():
    request_body = request.json
    if JSON_KEY_LOGIN not in request_body or JSON_KEY_FINGERPRINT not in request_body:
        response = Response(status=RESPONSE_CODE_BAD_REQUEST, response=ERROR_MESSAGE_INVALID_REQUEST_BODY)
        return response

    login = request_body[JSON_KEY_LOGIN]
    fingerprint = request_body[JSON_KEY_FINGERPRINT]

    return JwtHandler.logout(login, fingerprint)
