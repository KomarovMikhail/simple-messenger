from auth_server.logging_utils.loggers.metaclass_logger import MetaclassLogger
from auth_server.const.const import LOGGER_KEY_DB


class DbLogger(metaclass=MetaclassLogger, logger_key=LOGGER_KEY_DB):
    pass
