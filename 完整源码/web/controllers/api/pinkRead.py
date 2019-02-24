# -*- coding: utf-8 -*-
from web.controllers.api import route_api
from flask import request,jsonify,g
from common.libs.Helper import ops_render,iPagination,getCurrentDate
from common.models.pinkRead.PinkRead import ( TWechatPinkread )
from application import app,db
from common.libs.Helper import selectFilterObj,getDictFilterField,getCurrentDate,getCurrentDayDate

@route_api.route("/pinkRead/upload",methods = ["POST" ])
def uploadInfo():
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}

    req = request.values
    member_info = g.member_info
    ST_WECHATID = member_info.id
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

@route_api.route("/pinkRead/selfUploadList")
def myUploadList():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    member_info = g.member_info
    comment_list = TWechatPinkread.query.filter_by( ST_WECHATID=member_info.id ).order_by(TWechatPinkread.DT_STARTDATE.desc()).all()
    data_comment_list = []
    if comment_list:
        for item in comment_list:
            tmp_data = {
                "DT_STARTDATE":item.DT_STARTDATE.strftime("%Y-%m-%d"),
                "ST_GZHURL":item.ST_GZHURL
            }
            data_comment_list.append( tmp_data )
    resp['data']['list'] = data_comment_list
    return jsonify(resp)


@route_api.route("/pinkRead/checkUpload",methods = ["POST" ] )
def checkUpload():
    resp = {'code': 200, 'msg': '当日未上报~', 'data': {}}
    member_info = g.member_info
    nowDate=getCurrentDayDate()
    uploadInfo = TWechatPinkread.query.filter_by( ST_WECHATID=member_info.id,DT_STARTDATE=getCurrentDayDate() ).first()
    if uploadInfo:
        resp['code'] = -1
        resp['msg'] = "当日已上报"
        return jsonify(resp)
    return jsonify(resp)

