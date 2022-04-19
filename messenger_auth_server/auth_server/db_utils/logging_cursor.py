import psycopg2
import psycopg2.extensions
from auth_server.logging_utils.logger_factory import LoggerFactory
from auth_server.const.const import LOGGER_KEY_DB


class LoggingCursor(psycopg2.extensions.cursor):
    def execute(self, sql, args=None):
        logger = LoggerFactory.get_logger(LOGGER_KEY_DB)
        logger.log("Executing: {query}".format(query=self.mogrify(sql, args)))

        try:
            psycopg2.extensions.cursor.execute(self, sql, args)
        except Exception as e:
            logger.log("Occurred {exception}: {message}".format(exception=e.__class__.__name__, message=e))
            raise
