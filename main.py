#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Author  : yhma
# @contact: yhma.dev@outlook.com
# @Time    : 2019/12/6 21:21
# @File    : main.py
from be import create_app

app = create_app()

if __name__ == '__main__':
    # 日志记录当前环境配置名称
    # app.logger.info('flask app name = {} '.format(app.name))
    # app.logger.info('active config name = {} '.format())
    # # 启动flask应用app
    # server_port = app.config.get('SERVER_PORT')
    app.run(host='127.0.0.1')
