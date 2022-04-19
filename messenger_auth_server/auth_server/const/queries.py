USER_DATA_SELECT_USER_ID = "SELECT id FROM user_data WHERE login = '{login}'"
USER_DATA_INSERT_USER = "INSERT INTO user_data (id, login, password) VALUES ('{id}', '{login}', '{password}')"
USER_DATA_DELETE_USER = "DELETE FROM user_data WHERE id = '{id}'"
USER_DATA_SELECT_USER_DATA = "SELECT id, password FROM user_data WHERE login = '{login}'"

REFRESH_TOKEN_DATA_SELECT_REFRESH_SESSION_ID = \
    "SELECT id FROM refresh_token_data WHERE user_id = '{user_id}' AND fingerprint = '{fingerprint}'"
REFRESH_TOKEN_DATA_INSERT_REFRESH_SESSION = \
    "INSERT INTO refresh_token_data (id, user_id, refresh_token, fingerprint, creation_time, expiration_time) " \
    "VALUES ('{id}', '{user_id}', '{refresh_token}', '{fingerprint}', {creation_time}, {expiration_time})" \
    "ON CONFLICT (id) DO UPDATE " \
    "    SET refresh_token = excluded.refresh_token, creation_time = excluded.creation_time, " \
    "    expiration_time = excluded.expiration_time"
REFRESH_TOKEN_DATA_SELECT_REFRESH_SESSION_DATA = \
    "SELECT id, user_id, expiration_time FROM refresh_token_data " \
    "WHERE refresh_token = '{refresh_token}' AND fingerprint = '{fingerprint}'"
REFRESH_TOKEN_DATA_DELETE_REFRESH_SESSION = "DELETE FROM refresh_token_data WHERE id = '{id}';"
REFRESH_TOKEN_DATA_DELETE_USER_REFRESH_SESSION = "DELETE FROM refresh_token_data " \
                                                 "WHERE user_id = '{user_id}' AND fingerprint = '{fingerprint}';"
LISTEN_USER_DELETED = "LISTEN user_deleted"
