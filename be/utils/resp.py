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


def generate_resp_order(code, message):
    resp = jsonify(order_id=message)
    resp.status_code = code
    return resp

def generate_resp_store(code,store_list):
    resp = jsonify(store_list=store_list)
    resp.status_code = code
    return resp

def generate_resp_his_order(code, message):
    resp = jsonify(order=message)
    resp.status_code = code
    return resp

def generate_resp_goods(code,goods_list):
    resp = jsonify(goods_list=goods_list)
    resp.status_code = code
    return resp

def generate_resp_search(code,search_result):
    resp = jsonify(search_result=search_result)
    resp.status_code = code
    return resp