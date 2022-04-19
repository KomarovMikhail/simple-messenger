from auth_server.common_utils.singleton_metaclass import SingletonMetaclass
from auth_server.const.const import WEBHOOKS_PATH, USER_DELETED_WEBHOOKS_FILE_NAME
import os
from filelock import FileLock


class UserDeletedWebhookHandler(metaclass=SingletonMetaclass):
    def __init__(self):
        self._file_path = "{webhooks_path}/{file_name}" \
            .format(webhooks_path=WEBHOOKS_PATH, file_name=USER_DELETED_WEBHOOKS_FILE_NAME)
        self._lockfile_path = self._file_path + '.lock'

        try:
            os.makedirs(WEBHOOKS_PATH)
            file = open(self._file_path, 'a+')
            file.close()
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass

    def add_webhook(self, url):
        file_lock = FileLock(self._lockfile_path)
        with file_lock.acquire():
            with open(self._file_path, 'r+') as file:
                webhooks = file.readlines()
                url_new_line = url + '\n'
                if url_new_line in webhooks:
                    return False

                file.write(url_new_line)

        return True

    def remove_webhook(self, url):
        file_lock = FileLock(self._lockfile_path)
        with file_lock.acquire():
            with open(self._file_path, 'r') as file:
                webhooks = file.readlines()
                url_new_line = url + '\n'
                if url_new_line not in webhooks:
                    return False

            webhooks.remove(url_new_line)
            with open(self._file_path, 'w') as file:
                file.writelines(webhooks)

        return True
