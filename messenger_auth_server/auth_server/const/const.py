SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5433

API_PREFIX = '/api/auth'

REGISTER_URL = API_PREFIX + '/register'
LOGIN_URL = API_PREFIX + '/login'
REFRESH_TOKENS_URL = API_PREFIX + '/refresh-tokens'
LOGOUT_URL = API_PREFIX + '/logout'
DELETE_USER_URL = API_PREFIX + '/delete-user'
LOGS_URL = API_PREFIX + '/logs'
ADD_USER_DELETED_WEBHOOK_URL = API_PREFIX + '/add-user-deleted-webhook'
REMOVE_USER_DELETED_WEBHOOK_URL = API_PREFIX + '/remove-user-deleted-webhook'
ROOT_URL = '/'

JSON_KEY_LOGIN = 'login'
JSON_KEY_PASSWORD = 'password'
JSON_KEY_ACCESS_TOKEN = 'access-token'
JSON_KEY_REFRESH_TOKEN = 'refresh-token'
JSON_KEY_FINGERPRINT = 'fingerprint'
JSON_KEY_USER_ID = 'user-id'
JSON_KEY_WEBHOOK = 'webhook'

ARGUMENT_LOG_TYPE = 'log-type'
ARGUMENT_ROW_NUMBER = 'row-number'

JWT_KEY_ISS = 'iss'
JWT_KEY_AUD = 'aud'
JWT_KEY_IAT = 'iat'
JWT_KEY_EXP = 'exp'
JWT_KEY_USER_ID = 'user-id'

JWT_ISSUER = 'messenger-auth-server'
JWT_AUDIENCE = 'messenger-auth-server'

SERVER_SECRET_KEY = 'messenger-server-secret-key'

JWT_ALGORITHM = 'HS256'

ACCESS_TOKEN_LIFETIME = 60 * 10  # 10 minutes
REFRESH_TOKEN_LIFETIME = 60 * 60 * 24 * 30  # 1 month

HEADER_VALUE_APPLICATION_JSON = 'application/json'

MESSENGER_USER_DB_NAME = 'messenger-users-db'
MESSENGER_USER_DB_USER = 'postgres'
MESSENGER_USER_DB_PASSWORD = '0000'
MESSENGER_USER_DB_HOST = 'messenger-users-db-container'
# MESSENGER_USER_DB_HOST = 'localhost'
MESSENGER_USER_DB_PORT = 5432

MESSENGER_WORKDIR = 'messenger-auth-server-workdir'

LOGS_PATH = MESSENGER_WORKDIR + '/logs'
LOGGER_KEY_DB = 'logs-db'

WEBHOOKS_PATH = MESSENGER_WORKDIR + '/webhooks'
USER_DELETED_WEBHOOKS_FILE_NAME = 'user-deleted-webhooks'
