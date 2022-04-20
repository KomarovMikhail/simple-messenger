import jwt
import uuid
import hashlib
import json
import time
from auth_server.jwt_utils.users_db_handler import UsersDbHandler
from auth_server.const.error_messages import *
from auth_server.const.http_codes import *
from auth_server.const.const import HEADER_VALUE_APPLICATION_JSON, JSON_KEY_ACCESS_TOKEN, JSON_KEY_REFRESH_TOKEN, \
    JWT_KEY_ISS, JWT_KEY_AUD, JWT_KEY_IAT, JWT_KEY_EXP, JWT_KEY_USER_ID, JWT_ISSUER, JWT_AUDIENCE, \
    ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME, SERVER_SECRET_KEY, JWT_ALGORITHM
from auth_server.webhook_utils.user_deleted_webhook_handler import UserDeletedWebhookHandler

from flask import Response


class JwtHandler:
    @staticmethod
    def _generate_tokens(user_id, fingerprint):
        creation_time = int(time.time())
        access_token_expiration_time = creation_time + ACCESS_TOKEN_LIFETIME
        refresh_token_expiration_time = creation_time + REFRESH_TOKEN_LIFETIME

        payload = {
            JWT_KEY_ISS: JWT_ISSUER,
            JWT_KEY_AUD: JWT_AUDIENCE,
            JWT_KEY_IAT: creation_time,
            JWT_KEY_EXP: access_token_expiration_time,
            JWT_KEY_USER_ID: user_id
        }

        access_token = jwt.encode(payload, SERVER_SECRET_KEY, algorithm=JWT_ALGORITHM)
        refresh_token = str(uuid.uuid4())

        UsersDbHandler.insert_refresh_handler(user_id, refresh_token, fingerprint, creation_time,
                                              refresh_token_expiration_time)

        return access_token, refresh_token

    @staticmethod
    def register(login, password):
        user_id = str(uuid.uuid4())
        encrypted_password = hashlib.md5(password.encode()).hexdigest()
        success_flag = UsersDbHandler.insert_user(user_id, login, encrypted_password)

        if not success_flag:
            return Response(
                status=RESPONSE_CODE_INTERNAL_SERVER_ERROR,
                response=ERROR_MESSAGE_USER_ALREADY_EXISTS)

        return Response(status=RESPONSE_CODE_OK)

    @staticmethod
    def delete_user(login):
        success_flag,  user_id = UsersDbHandler.delete_user(login)

        if not success_flag:
            return Response(
                status=RESPONSE_CODE_INTERNAL_SERVER_ERROR,
                response=ERROR_MESSAGE_USER_NOT_EXISTS_ON_DELETE)

        UserDeletedWebhookHandler().notify(user_id)

        return Response(status=RESPONSE_CODE_OK)

    @staticmethod
    def login(login, password, fingerprint):
        encrypted_password = hashlib.md5(password.encode()).hexdigest()
        success_flag, user_id, stored_encrypted_password = UsersDbHandler.get_user_data(login)

        if not success_flag:
            return Response(status=RESPONSE_CODE_UNAUTHORIZED, response=ERROR_MESSAGE_USER_NOT_EXISTS_ON_LOGIN)

        if stored_encrypted_password != encrypted_password:
            return Response(status=RESPONSE_CODE_UNAUTHORIZED, response=ERROR_MESSAGE_WRONG_PASSWORD)

        access_token, refresh_token = JwtHandler._generate_tokens(user_id, fingerprint)

        return Response(
            status=RESPONSE_CODE_OK,
            response=json.dumps({JSON_KEY_ACCESS_TOKEN: access_token, JSON_KEY_REFRESH_TOKEN: refresh_token}),
            content_type=HEADER_VALUE_APPLICATION_JSON)

    @staticmethod
    def refresh_tokens(refresh_token, fingerprint):
        success_flag, user_id, expiration_time = UsersDbHandler.get_refresh_session_data(refresh_token, fingerprint)

        if not success_flag:
            return Response(status=RESPONSE_CODE_UNAUTHORIZED, response=ERROR_MESSAGE_REFRESH_SESSION_NOT_EXISTS)

        current_time = int(time.time())
        if current_time > expiration_time:
            return Response(status=RESPONSE_CODE_UNAUTHORIZED, response=ERROR_MESSAGE_REFRESH_TOKEN_EXPIRED)

        access_token, refresh_token = JwtHandler._generate_tokens(user_id, fingerprint)

        return Response(
            status=RESPONSE_CODE_OK,
            response=json.dumps({JSON_KEY_ACCESS_TOKEN: access_token, JSON_KEY_REFRESH_TOKEN: refresh_token}),
            content_type=HEADER_VALUE_APPLICATION_JSON)

    @staticmethod
    def logout(login, fingerprint):
        success_flag = UsersDbHandler.delete_user_session(login, fingerprint)

        if not success_flag:
            return Response(
                status=RESPONSE_CODE_INTERNAL_SERVER_ERROR,
                response=ERROR_MESSAGE_DELETE_REFRESH_SESSION)

        return Response(status=RESPONSE_CODE_OK)
