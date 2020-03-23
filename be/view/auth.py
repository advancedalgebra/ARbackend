#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hjcao
# @contact: redpeanut@163.com
# @Time    : 2020/3/21 17:21
# @File    : auth.py
from flask import Blueprint, session, escape, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import be as app
from be.utils.config import *
from be.utils.resp import generate_resp
from be.utils.token import *

db = app.db
User = app.User


bp = Blueprint('/ar/api/auth', __name__)


@bp.route('/register', methods=['POST'])
def register():
    json = request.json
    username = json['username']
    password = json['password']
    password_again = json['password_again']
    if User.query.filter_by(username=username).first():
        resp = generate_resp(FAIL, '注册失败, 用户名重复')
        return resp
    if password != password_again:
        resp = generate_resp(FAIL, '注册失败, 密码不一致')
        return resp
    else:
        hashed_pwd = generate_password_hash(password)
        new_user = User(username, hashed_pwd)
        db.session.add(new_user)
        db.session.commit()
        resp = generate_resp(SUCCESS, 'ok')
        return resp


@bp.route('/unregister', methods=['POST'])
def unregister():
    json = request.json
    username = json['username']
    password = json['password']
    user = User.query.filter_by(username=username).first()
    if user is None:
        resp = generate_resp(FAIL, '注销失败，用户名不存在')
    elif not check_password_hash(user.password, password):
        resp = generate_resp(FAIL, '注销失败，密码不正确')
    else:
        db.session.delete(user)
        db.session.commit()
        resp = generate_resp(SUCCESS, 'ok')
    return resp


@bp.route('/login', methods=['POST'])
def login():
    json = request.json
    username = json['username']
    password = json['password']
    user = User.query.filter_by(username=username).first()
    if user is None:
        resp = generate_resp(FAIL, '登录失败，用户名不存在!')
    elif not check_password_hash(user.password, password):
        resp = generate_resp(FAIL, '登录失败，密码错误')
    else:
        token = jwt_encode(username)
        user.token = token
        db.session.commit()
        resp = jsonify(message="ok", token=token)
        resp.status_code = SUCCESS
    return resp


@bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('token')
    if token == "":
        resp = generate_resp(FAIL, "查询失败, token错误")
        return resp
    username = request.json.get("username", "")
    # token可能有错
    de_token = jwt_decode(token)
    # print(de_token)
    if de_token is None:
        resp = generate_resp(FAIL, "查询失败, token错误")
        return resp
    if de_token['user_id'] != username:
        resp = generate_resp(FAIL, "登出失败, token错误")
    else:
        user = User.query.filter_by(username=username).first()
        if user is None:
            resp = generate_resp(FAIL, "登出失败, 用户名错误")
        elif user.token:
            user.token = None
            db.session.commit()
            resp = generate_resp(SUCCESS, 'ok')
        else:
            resp = generate_resp(FAIL, "登出失败, 不要重复登出")
    return resp


@bp.route('/password', methods=['POST'])
def change_pwd():
    json = request.json
    username = json['username']
    old_password = json['oldPassword']
    new_password = json['newPassword']
    user = User.query.filter_by(username=username).first()
    if user is None:
        resp = generate_resp(FAIL, "修改失败, 用户名不存在")
    elif not check_password_hash(user.password, old_password):
        resp = generate_resp(FAIL, "修改失败, 密码错误")
    else:
        user.password = generate_password_hash(new_password)
        db.session.commit()
        resp = generate_resp(SUCCESS, "ok")
    return resp
