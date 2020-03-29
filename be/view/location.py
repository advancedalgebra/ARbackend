#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hjcao
# @contact: redpeanut@163.com
# @Time    : 2019/12/18 12:36
# @File    : location.py
from operator import and_

from flask import Blueprint, request
from werkzeug.security import check_password_hash
import be as app
from be.utils.config import *
from be.utils.resp import *
from be.utils.token import *


db = app.db
User = app.User
Building = app.Building

bp = Blueprint('/ar/api/location', __name__)


@bp.route('/building_id', methods=['POST'])
def building_id():
    result = []
    json = request.json
    latitude = json['latitude']
    longitude = json['longitude']
    building_all = Building.query.filter(and_(Building.latitude_lower < latitude, Building.latitude_upper > latitude)).\
        filter(and_(Building.longitude_lower < longitude, Building.longitude_upper > longitude)).all()
    for building in building_all:
        result.append({'id': building.building_id, 'name':  building.name})
    if len(result) == 0:
        resp = generate_resp(FAIL, '没有查找到相关建筑')
    else:
        resp = generate_resp_building(SUCCESS, result)
    return resp


@bp.route('/building_id_token', methods=['POST'])
def building_id_token():
    token = request.headers.get('token')
    if token == "":
        resp = generate_resp(FAIL, "查询失败, token错误")
        return resp
    username = request.json.get("username", "")
    # token可能有错
    de_token = jwt_decode(token)
    if de_token is None:
        resp = generate_resp(FAIL, "查询失败, token错误")
        return resp
    # print(de_token)
    if de_token['user_id'] != username:
        resp = generate_resp(FAIL, "查询失败, token错误")
    else:
        user = User.query.filter_by(username=username).first()
        if user is None:
            resp = generate_resp(FAIL, "查询失败, 用户名错误")
        elif user.token:
            result = []
            json = request.json
            latitude = json['latitude']
            longitude = json['longitude']
            building_all = Building.query.filter(
                and_(Building.latitude_lower < latitude, Building.latitude_upper > latitude)). \
                filter(and_(Building.longitude_lower < longitude, Building.longitude_upper > longitude)).all()
            for building in building_all:
                result.append({'id': building.building_id, 'name':  building.name})
            if len(result) == 0:
                resp = generate_resp(FAIL, '没有查找到相关建筑')
            else:
                resp = generate_resp_building(SUCCESS, result)
        else:
            resp = generate_resp(FAIL, "查询失败, 未登录")
    return resp


@bp.route('/building_detail', methods=['POST'])
def building_detail():
    json = request.json
    building_id_ = json['building_id']
    temp = Building.query.filter_by(building_id=building_id_).first()
    if temp:
        resp = generate_resp_description(SUCCESS, temp.description)
    else:
        resp = generate_resp(FAIL, '该建筑不存在')
    return resp


@bp.route('/building_detail_token', methods=['POST'])
def building_detail_token():
    token = request.headers.get('token')
    if token == "":
        resp = generate_resp(FAIL, "查询失败, token错误")
        return resp
    username = request.json.get("username", "")
    # token可能有错
    de_token = jwt_decode(token)
    if de_token is None:
        resp = generate_resp(FAIL, "查询失败, token错误")
        return resp
    # print(de_token)
    if de_token['user_id'] != username:
        resp = generate_resp(FAIL, "查询失败, token错误")
    else:
        user = User.query.filter_by(username=username).first()
        if user is None:
            resp = generate_resp(FAIL, "查询失败, 用户名错误")
        elif user.token:
            json = request.json
            building_id_ = json['building_id']
            temp = Building.query.filter_by(building_id=building_id_).first()
            if temp:
                resp = generate_resp_description(SUCCESS, temp.description)
            else:
                resp = generate_resp(FAIL, '该建筑不存在')
        else:
            resp = generate_resp(FAIL, "查询失败, 未登录")
    return resp
