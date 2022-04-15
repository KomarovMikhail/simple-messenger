from auth_server import app
from auth_server.const.const import DELETE_USER_URL, JSON_KEY_LOGIN
from auth_server.const.http_codes import RESPONSE_CODE_BAD_REQUEST
from auth_server.const.error_messages import ERROR_MESSAGE_INVALID_REQUEST_BODY
from auth_server.jwt_utils.jwt_handler import JwtHandler

from flask import request
from flask import Response


@app.route(DELETE_USER_URL, methods=['POST'])
def delete_user_controller():
    request_body = request.json
    if JSON_KEY_LOGIN not in request_body:
        return Response(response=ERROR_MESSAGE_INVALID_REQUEST_BODY, status=RESPONSE_CODE_BAD_REQUEST)

    login = request_body[JSON_KEY_LOGIN]

    return JwtHandler.delete_user(login)
