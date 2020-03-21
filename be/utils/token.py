#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Author  : yhma
# @contact: yhma.dev@outlook.com
# @Time    : 2019/12/6 20:03
# @File    : token.py
import jwt
import time
from be.utils.config import SECRET_KEY


def jwt_encode(user_id, terminal):
    encoded = jwt.encode(
        {"user_id": user_id, "terminal": terminal, "timestamp": time.time()},
        key=SECRET_KEY,
        algorithm="HS256",
    )
    return encoded.decode("utf-8")


def jwt_decode(encoded_token):
    try:
        decoded = jwt.decode(encoded_token, key=SECRET_KEY, algorithms="HS256")
        return decoded
    except Exception as e:
        return None
