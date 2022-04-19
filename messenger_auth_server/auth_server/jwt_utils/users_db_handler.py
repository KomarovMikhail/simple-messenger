import psycopg2
import uuid
from auth_server.const.const import MESSENGER_USER_DB_NAME, MESSENGER_USER_DB_USER, MESSENGER_USER_DB_PASSWORD, \
    MESSENGER_USER_DB_HOST, MESSENGER_USER_DB_PORT
from auth_server.const.queries import *
from auth_server.db_utils.logging_cursor import LoggingCursor


class UsersDbHandler:

    class RefreshSessionNotExistsError(Exception):
        pass

    @staticmethod
    def _get_connection():
        return psycopg2.connect(
            dbname=MESSENGER_USER_DB_NAME,
            user=MESSENGER_USER_DB_USER,
            password=MESSENGER_USER_DB_PASSWORD,
            host=MESSENGER_USER_DB_HOST,
            port=MESSENGER_USER_DB_PORT)

    @staticmethod
    def insert_user(user_id, login, password):
        result = False
        connection = UsersDbHandler._get_connection()

        try:
            with connection:
                with connection.cursor(cursor_factory=LoggingCursor) as cursor:
                    cursor.execute(USER_DATA_SELECT_USER_ID.format(login=login))
                    response = cursor.fetchall()

                    if not response:
                        cursor.execute(USER_DATA_INSERT_USER.format(id=user_id, login=login, password=password))
                        result = True
        finally:
            connection.close()

        return result

    @staticmethod
    def delete_user(login):
        result = False
        connection = UsersDbHandler._get_connection()

        try:
            with connection:
                with connection.cursor(cursor_factory=LoggingCursor) as cursor:
                    cursor.execute(USER_DATA_SELECT_USER_ID.format(login=login))
                    response = cursor.fetchall()

                    if response:
                        user_id = response[0][0]
                        cursor.execute(USER_DATA_DELETE_USER.format(id=user_id))
                        result = True
        finally:
            connection.close()

        return result

    @staticmethod
    def get_user_data(login):
        result = False
        user_id = ''
        password = ''
        connection = UsersDbHandler._get_connection()

        try:
            with connection:
                with connection.cursor(cursor_factory=LoggingCursor) as cursor:
                    cursor.execute(USER_DATA_SELECT_USER_DATA.format(login=login))
                    response = cursor.fetchall()

                    if response:
                        user_id = response[0][0]
                        password = response[0][1]
                        result = True
        finally:
            connection.close()

        return result, user_id, password

    @staticmethod
    def insert_refresh_handler(user_id, refresh_token, fingerprint, creation_time, expiration_time):
        result = False
        connection = UsersDbHandler._get_connection()

        try:
            with connection:
                with connection.cursor(cursor_factory=LoggingCursor) as cursor:
                    cursor.execute(REFRESH_TOKEN_DATA_SELECT_REFRESH_SESSION_ID.format(
                        user_id=user_id,
                        fingerprint=fingerprint))
                    response = cursor.fetchall()

                    refresh_session_id = str(uuid.uuid4())
                    if response:
                        refresh_session_id = response[0][0]

                    cursor.execute(REFRESH_TOKEN_DATA_INSERT_REFRESH_SESSION.format(
                        id=refresh_session_id,
                        user_id=user_id,
                        refresh_token=refresh_token,
                        fingerprint=fingerprint,
                        creation_time=creation_time,
                        expiration_time=expiration_time))

                    result = True
        finally:
            connection.close()

        return result

    @staticmethod
    def get_refresh_session_data(refresh_token, fingerprint):
        result = False
        user_id = ''
        expiration_time = -1
        connection = UsersDbHandler._get_connection()

        try:
            with connection:
                with connection.cursor(cursor_factory=LoggingCursor) as cursor:
                    cursor.execute(REFRESH_TOKEN_DATA_SELECT_REFRESH_SESSION_DATA.format(
                        refresh_token=refresh_token,
                        fingerprint=fingerprint))
                    response = cursor.fetchall()

                    if not response:
                        raise UsersDbHandler.RefreshSessionNotExistsError

                    refresh_session_id = response[0][0]
                    user_id = response[0][1]
                    expiration_time = response[0][2]

                    cursor.execute(REFRESH_TOKEN_DATA_DELETE_REFRESH_SESSION.format(id=refresh_session_id))

                    result = True
        except UsersDbHandler.RefreshSessionNotExistsError:
            pass
        finally:
            connection.close()

        return result, user_id, expiration_time

    @staticmethod
    def delete_user_session(login, fingerprint):
        result = False
        connection = UsersDbHandler._get_connection()

        try:
            with connection:
                with connection.cursor(cursor_factory=LoggingCursor) as cursor:
                    cursor.execute(USER_DATA_SELECT_USER_ID.format(login=login))
                    response = cursor.fetchall()

                    if response:
                        user_id = response[0][0]
                        cursor.execute(REFRESH_TOKEN_DATA_DELETE_USER_REFRESH_SESSION.format(
                            user_id=user_id,
                            fingerprint=fingerprint))

                        result = True
        finally:
            connection.close()

        return result
