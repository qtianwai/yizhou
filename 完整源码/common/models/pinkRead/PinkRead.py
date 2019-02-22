# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db,app

class TWechatPinkread(db.Model):
    __tablename__ = 't_wechat_pinkread'

    NM_SID = db.Column(db.Integer, primary_key=True)
    DT_STARTDATE = db.Column(db.Date)
    DT_ENDDATE = db.Column(db.Date)
    ST_QQID = db.Column(db.String(200))
    ST_WECHATID = db.Column(db.String(255))
    ST_DAIDING = db.Column(db.String(255))
    ST_GROUPUSERNAME = db.Column(db.String)
    ST_GZHNAME = db.Column(db.String(255))
    ST_GZHTYPE = db.Column(db.String(255))
    ST_GZHURL = db.Column(db.String)
    ST_GROUPNAME = db.Column(db.String(255))
