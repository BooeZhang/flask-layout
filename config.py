#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import yaml


def load_log():
    """ 加载 log 配置文件 """
    with open("conf/log.yaml", 'r', encoding='utf8') as f:
        return yaml.safe_load(f)


def load_service_conf():
    """ 加载 flask 配置文件 """

    if os.environ.get('FLASK_DEBUG'):
        with open('conf/config-prod.yaml', 'r', encoding='utf8') as f:
            return yaml.safe_load(f)
    else:
        with open('conf/config-dev.yaml', 'r', encoding='utf8') as f:
            return yaml.safe_load(f)


cf = load_service_conf()
