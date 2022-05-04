#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import db


class UserModel(db.Model):
    """
    user表
    """

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        """
        输出好阅读的字符串
        """
        return f'<User {self.username}>'
