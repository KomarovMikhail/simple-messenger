from auth_server import app
from auth_server.const.const import ROOT_URL
from auth_server.const.http_codes import RESPONSE_CODE_OK

from flask import Response


@app.route(ROOT_URL, methods=['GET'])
def root_controller():
    return Response(status=RESPONSE_CODE_OK)
