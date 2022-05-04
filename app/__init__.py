#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

from config import cf

app = Flask(__name__)
db = SQLAlchemy()
redis_client = FlaskRedis()


def make_app():
    app.config.update(cf)
    CORS(app, supports_credentials=True)
    db.init_app(app)
    redis_client.init_app(app)
    register(app)

    return app


def register(application):
    """
    蓝图注册
    所有声明的蓝图必须在此处注册才能使用
    """
    from app.user import user
    application.register_blueprint(user, url_prefix='/v1/user')
