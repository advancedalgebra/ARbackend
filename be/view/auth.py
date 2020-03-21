#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Author  : yhma
# @contact: yhma.dev@outlook.com
# @Time    : 2019/12/3 15:38
# @File    : auth.py
from flask import Blueprint, session, escape, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import be as app
from be.utils.config import *
from be.utils.resp import generate_resp
from be.utils.token import *

db = app.db
User = app.User


bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['POST'])
def add_user():
    json = request.json
    user_id = json['user_id']
    password = json['password']

    if User.query.filter_by(user_id=user_id).first():
        resp = generate_resp(FAIL, '注册失败, 用户名重复')
        return resp
    else:
        # TODO 数据库插入是否要增加异常判断?
        hashed_pwd = generate_password_hash(password)
        new_user = User(user_id, hashed_pwd)
        db.session.add(new_user)
        db.session.commit()
        resp = generate_resp(SUCCESS, 'ok')
        return resp


@bp.route('/unregister', methods=['POST'])
def unregister():
    json = request.json
    user_id = json['user_id']
    password = json['password']
    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        resp = generate_resp(FAIL, '注销失败，用户名不存在')
    elif not check_password_hash(user.password, password):
        resp = generate_resp(FAIL, '注销失败，密码不正确')
    else:
        db.session.delete(user)
        db.session.commit()
        resp = generate_resp(SUCCESS, 'ok')
    return resp


# @bp.errorhandler(404)
# def not_found(error=None):
#     message = {
#         'status': 404,
#         'message': 'Not Found: ' + request.url,
#     }
#     resp = jsonify(message)
#     resp.status_code = 404
#
#     return resp

@bp.route('/login', methods=['POST'])
def login():
    json = request.json
    user_id = json['user_id']
    password = json['password']
    terminal = json['terminal']
    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        resp = generate_resp(FAIL, '登录失败，用户名不存在!')
    elif not check_password_hash(user.password, password):
        resp = generate_resp(FAIL, '登录失败，密码错误')
    else:
        token = jwt_encode(user_id, terminal)
        user.terminal = terminal
        user.token = token
        db.session.commit()
        resp = jsonify(message="ok", token=token)
        resp.status_code = SUCCESS
    return resp


@bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('token')
    user_id = request.json.get("user_id", "")
    # token可能有错
    de_token = jwt_decode(token)
    if de_token is None:
        resp = generate_resp(FAIL, "登出失败, token错误")
    else:
        terminal = de_token['terminal']
        user = User.query.filter_by(user_id=user_id, terminal=terminal).first()
        if user is None:
            resp = generate_resp(FAIL, "登出失败, 用户名错误")
        else:
            user.token = None
            db.session.commit()
            resp = generate_resp(SUCCESS, 'ok')
    return resp


@bp.route('/password', methods=['POST'])
def change_pwd():
    json = request.json
    user_id = json['user_id']
    old_password = json['oldPassword']
    new_password = json['newPassword']
    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        resp = generate_resp(FAIL, "修改失败, 用户名不存在")
    elif not check_password_hash(user.password, old_password):
        resp = generate_resp(FAIL, "修改失败, 密码错误")
    else:
        user.password = generate_password_hash(new_password)
        db.session.commit()
        resp = generate_resp(SUCCESS, "ok")
    return resp
