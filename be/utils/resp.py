#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Author  : yhma, hjcao
# @contact: yhma.dev@outlook.com, redpeanut@163.com
# @Time    : 2020/3/21 17:21
# @File    : resp.py

from flask import jsonify


def generate_resp(code, message):
    resp = jsonify(message=message)
    resp.status_code = code
    return resp


def generate_resp_building(code, message):
    resp = jsonify(building_list=message)
    resp.status_code = code
    return resp


def generate_resp_description(code, message):
    resp = jsonify(description=message)
    resp.status_code = code
    return resp
