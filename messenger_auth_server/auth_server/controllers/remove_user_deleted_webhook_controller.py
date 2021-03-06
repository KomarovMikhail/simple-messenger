from auth_server import app
from auth_server.const.const import REMOVE_USER_DELETED_WEBHOOK_URL, JSON_KEY_WEBHOOK
from auth_server.const.http_codes import RESPONSE_CODE_BAD_REQUEST, RESPONSE_CODE_OK
from auth_server.const.error_messages import ERROR_MESSAGE_WEBHOOK_NOT_EXISTS, ERROR_MESSAGE_INVALID_REQUEST_BODY
from auth_server.webhook_utils.user_deleted_webhook_handler import UserDeletedWebhookHandler

from flask import request
from flask import Response


@app.route(REMOVE_USER_DELETED_WEBHOOK_URL, methods=['POST'])
def remove_user_deleted_controller():
    request_body = request.json
    if JSON_KEY_WEBHOOK not in request_body:
        return Response(status=RESPONSE_CODE_BAD_REQUEST, response=ERROR_MESSAGE_INVALID_REQUEST_BODY)

    webhook = request_body[JSON_KEY_WEBHOOK]
    webhook_removed_success = UserDeletedWebhookHandler().remove_webhook(webhook)
    if not webhook_removed_success:
        return Response(status=RESPONSE_CODE_BAD_REQUEST, response=ERROR_MESSAGE_WEBHOOK_NOT_EXISTS)

    return Response(status=RESPONSE_CODE_OK, response='')
