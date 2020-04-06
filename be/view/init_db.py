#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : hjcao
# @contact: redpeanut@163.com
# @Time    : 2020/4/6 14:52
# @File    : init_db.py
from flask import Blueprint
import be as app
from be.utils.resp import generate_resp
from be.utils.config import *

db = app.db
User = app.User
Event = app.Event
Building = app.Building

bp = Blueprint('/init', __name__)


# @bp.route('/event/<int:building_id>/<string:username>/<string:title>/<string:content>/<string:time>', methods=['GET'])
# def add_event(building_id, username, title, content, time):
#     new_event = Event(building_id, username, title, content, time)
#     db.session.add(new_event)
#     db.session.commit()
#     resp = generate_resp(SUCCESS, 'ok')
#     return resp
#
#
# @bp.route('/building/<float:latitude_upper>/<float:longitude_upper>/<float:latitude_lower>/<float:longitude_lower>/<string:name>/<string:description>', methods=['GET'])
# def add_building(latitude_upper, longitude_upper, latitude_lower, longitude_lower, name, description):
#     new_building = Building(latitude_upper, longitude_upper, latitude_lower, longitude_lower, name, description)
#     db.session.add(new_building)
#     db.session.commit()
#     resp = generate_resp(SUCCESS, 'ok')
#     return resp

latitude_upper_list = [31.233079, 31.235214]
longitude_upper_list = [121.410819, 121.414417]
latitude_lower_list = [31.231833, 31.235013]
longitude_lower_list = [121.410028, 121.410644]
name_list = ["华东师大三馆教学楼", "华东师大第八宿舍"]
description_list = ['过了丽娃河就是河西教学区，也就是理科生的天下了。主干道的尽头是师大最富有民族建筑特色的三馆。两翼楼护卫着正楼，气势宏大，歇山屋顶清平瓦，显得淡泊老成。新建造的理科大楼双子塔，与河东十八层的文科大楼，遥遥相望，形成华师大新的景观。和丽娃河东的文科教学区的浪漫氛围有所不同，这里弥漫的是一点严肃气息。馆前毛主席像下是一块休息用的草坪，据说是华师大社团经常活动的地方！',
                    '华东师大中北校区的一栋宿舍']

building_id_list = [1, 1, 1, 2, 2, 2]
username_list = ['jyh', 'jyh', 'jyh', 'jyh', 'jyh', 'jyh']
title_list = ['CV实验课', 'CV实验课', 'CV实验课', '吃泡面', '玩电脑', '睡觉']
content_list = ['KNN分类器的实现', 'SVM分类器的实现', '神经网络的实现', '写代码写的有点饿了', '放松一下，玩一把lol', '一天的结束']
time_list = ['2020-3-9', '2020-3-9', '2020-3-9', '2020-3-9', '2020-3-9', '2020-3-9']
@bp.route('/', methods=['GET'])
def init_db():
    for i in range(len(name_list)):
        new_building = Building(latitude_upper_list[i], longitude_upper_list[i], latitude_lower_list[i],
                                longitude_lower_list[i], name_list[i], description_list[i])
        db.session.add(new_building)
    for i in range(len(time_list)):
        new_event = Event(building_id_list[i], username_list[i], title_list[i], content_list[i], time_list[i])
        db.session.add(new_event)
    db.session.commit()
    resp = generate_resp(SUCCESS, 'ok')
    return resp


