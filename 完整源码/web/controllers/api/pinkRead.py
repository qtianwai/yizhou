# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify
from common.libs.Helper import ops_render,iPagination,getCurrentDate
from common.models.pinkRead.PinkRead import ( TWechatPinkread )
from application import app,db
route_upload = Blueprint('upload_page', __name__)

'''
参考文章：https://segmentfault.com/a/1190000002429055
'''

@route_upload.route("/pinkRead/upload",methods = [ "GET","POST" ])
def uploadInfo():
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}

    req = request.values
    ST_WECHATID = req['ST_WECHATID'] if 'ST_WECHATID' in req else ''
    ST_GROUPUSERNAME = req['ST_GROUPUSERNAME'] if 'ST_GROUPUSERNAME' in req else ''
    ST_GZHNAME = req['ST_GZHNAME'] if 'ST_GZHNAME' in req else ''
    ST_GZHTYPE = req['ST_GZHTYPE'] if 'ST_GZHTYPE' in req else ''
    ST_GZHURL = req['ST_GZHURL'] if 'ST_GZHURL' in req else ''
    ST_GROUPNAME = req['ST_GROUPNAME'] if 'ST_GROUPNAME' in req else ''
    model_pinkRead = TWechatPinkread()
    model_pinkRead.DT_STARTDATE = getCurrentDate()
    model_pinkRead.DT_ENDDATE = getCurrentDate()
    model_pinkRead.ST_WECHATID = ST_WECHATID
    model_pinkRead.ST_GROUPUSERNAME = ST_GROUPUSERNAME
    model_pinkRead.ST_GZHNAME = ST_GZHNAME
    model_pinkRead.ST_GZHTYPE = ST_GZHTYPE
    model_pinkRead.ST_GZHURL = ST_GZHURL
    model_pinkRead.ST_GROUPNAME = ST_GROUPNAME

    db.session.add(model_pinkRead)
    db.session.commit()
    return jsonify(resp)







