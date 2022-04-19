from auth_server.logging_utils.logger_factory import LoggerFactory
from auth_server.const.const import LOGS_PATH
from datetime import datetime
from filelock import FileLock
import os


class MetaclassLogger(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __new__(mcs, name, bases, namespace, **kwargs):
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace)
        logger_key = kwargs['logger_key']
        LoggerFactory.add_logger(logger_key, cls)
        cls._file_path = "{logs_path}/{file_name}".format(logs_path=LOGS_PATH, file_name=logger_key)
        cls._lockfile_path = cls._file_path + '.lock'
        try:
            os.makedirs(LOGS_PATH)
            file = open(cls._file_path, 'a+')
            file.close()
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass

    def log(cls, message):
        full_message = "{timestamp}: {message}".format(timestamp=datetime.now(), message=message)

        file_lock = FileLock(cls._lockfile_path)
        with file_lock.acquire():
            with open(cls._file_path, 'a+') as file:
                file.write(full_message + '\n')

    def get_last_logs(cls, row_number):
        file_lock = FileLock(cls._lockfile_path)
        try:
            with file_lock.acquire():
                with open(cls._file_path, 'r') as file:
                    result = ''.join(file.readlines()[-row_number:])
        except FileNotFoundError:
            return ''

        return result
