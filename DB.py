#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/1 14:45
# @File    : DB.py

"""
数据库配置
"""

from Start import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:123456789@localhost/mydata'#配置数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy()
db.init_app(app)