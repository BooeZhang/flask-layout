#!/usr/bin/python
# -*- coding: utf-8 -*-

from loguru import logger as log
from werkzeug.serving import WSGIRequestHandler

from app import make_app
from config import cf


def replace_request_handler_log(self, _type: str, message: str, path: str, code: int, *args):
    log.info(f"{self.address_string()}  [ {code} ]  {path}")


WSGIRequestHandler.log = replace_request_handler_log


if __name__ == '__main__':
    app = make_app()
    app.run(port=cf.get('PORT'))

