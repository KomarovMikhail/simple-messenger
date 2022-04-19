import select
import psycopg2
import requests
import psycopg2.extensions
import threading
from auth_server.const.const import MESSENGER_USER_DB_NAME, MESSENGER_USER_DB_USER, MESSENGER_USER_DB_PASSWORD, \
    MESSENGER_USER_DB_HOST, MESSENGER_USER_DB_PORT, USER_DELETED_WEBHOOKS_FILE_NAME, JSON_KEY_USER_ID
from auth_server.const.queries import LISTEN_USER_DELETED


class UserDeletedListener(threading.Thread):
    def run(self, *args, **kwargs):
        connection = psycopg2.connect(
            dbname=MESSENGER_USER_DB_NAME,
            user=MESSENGER_USER_DB_USER,
            password=MESSENGER_USER_DB_PASSWORD,
            host=MESSENGER_USER_DB_HOST,
            port=MESSENGER_USER_DB_PORT)
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()
        cursor.execute(LISTEN_USER_DELETED)

        while True:
            print("entering")
            select.select([connection], [], [])
            connection.poll()
            print("polling")
            while connection.notifies:
                notify = connection.notifies.pop()
                user_id = notify.payload
                print("in while")
                with open(USER_DELETED_WEBHOOKS_FILE_NAME, 'r') as file:
                    for url in file.readlines():
                        # requests.post(url, data={JSON_KEY_USER_ID: user_id})
                        print('requesting ' + url + ' ' + user_id)


def run_user_deleted_listener():
    user_deleted_listener = UserDeletedListener()
    user_deleted_listener.start()
