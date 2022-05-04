#!/usr/bin/python
# -*- coding: utf-8 -*-
from app.user import user


@user.get("/")
def index():
    return "ss"
