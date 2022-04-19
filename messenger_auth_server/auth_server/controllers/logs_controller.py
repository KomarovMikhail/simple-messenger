from auth_server import app
from auth_server.const.const import LOGS_URL, ARGUMENT_LOG_TYPE, ARGUMENT_ROW_NUMBER
from auth_server.const.http_codes import RESPONSE_CODE_BAD_REQUEST, RESPONSE_CODE_OK
from auth_server.const.error_messages import ERROR_MESSAGE_NO_LOG_TYPE, ERROR_MESSAGE_WRONG_LOG_TYPE
from auth_server.logging_utils.logger_factory import LoggerFactory

from flask import request
from flask import Response


@app.route(LOGS_URL, methods=['GET'])
def logs_controller():
    """
    Returns last <row-number> rows for logs of type <log-type>.
    If <row-number> not specified, returns last 100 rows
    """
    if ARGUMENT_LOG_TYPE not in request.args:
        return Response(status=RESPONSE_CODE_BAD_REQUEST, response=ERROR_MESSAGE_NO_LOG_TYPE)

    row_number = 100
    if ARGUMENT_ROW_NUMBER in request.args:
        row_number = int(request.args.get(ARGUMENT_ROW_NUMBER))
    log_type = request.args.get(ARGUMENT_LOG_TYPE)

    logger = LoggerFactory.get_logger(log_type)
    if not logger:
        return Response(status=RESPONSE_CODE_BAD_REQUEST, response=ERROR_MESSAGE_WRONG_LOG_TYPE)

    return Response(status=RESPONSE_CODE_OK, response=logger.get_last_logs(row_number))
