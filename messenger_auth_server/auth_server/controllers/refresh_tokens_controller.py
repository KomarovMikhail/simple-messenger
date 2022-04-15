from auth_server import app
from auth_server.const.const import REFRESH_TOKENS_URL, JSON_KEY_REFRESH_TOKEN, JSON_KEY_FINGERPRINT
from auth_server.const.http_codes import RESPONSE_CODE_BAD_REQUEST
from auth_server.const.error_messages import ERROR_MESSAGE_INVALID_REQUEST_BODY
from auth_server.jwt_utils.jwt_handler import JwtHandler

from flask import request
from flask import Response


@app.route(REFRESH_TOKENS_URL, methods=['POST'])
def refresh_tokens_controller():
    request_body = request.json
    if JSON_KEY_REFRESH_TOKEN not in request_body or JSON_KEY_FINGERPRINT not in request_body:
        response = Response(status=RESPONSE_CODE_BAD_REQUEST, response=ERROR_MESSAGE_INVALID_REQUEST_BODY)
        return response

    refresh_token = request_body[JSON_KEY_REFRESH_TOKEN]
    fingerprint = request_body[JSON_KEY_FINGERPRINT]

    return JwtHandler.refresh_tokens(refresh_token, fingerprint)
