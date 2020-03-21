#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hjcao
# @contact: redpeanut@163.com
# @Time    : 2019/12/18 12:36
# @File    : buyer.py
from flask import Blueprint, request
from werkzeug.security import check_password_hash
import be as app
import pymongo
import time
from bson.json_util import dumps
from be.utils.config import *
from be.utils.resp import *
from be.utils.token import *


db = app.db
User = app.User

bp = Blueprint('buyer', __name__)


