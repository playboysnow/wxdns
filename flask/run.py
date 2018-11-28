#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect
import urllib,requests,sys
import logging
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import json
reload(sys)
sys.setdefaultencoding('UTF-8')
#sys.setdefaultencoding('gb2312')

#handler=logging.FileHandler('run.log',encoding='UTF-8')

app=Flask(__name__, static_folder="./dist/static",
            template_folder="./dist")
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def index():

    return render_template("index.html")
#app.logger.addHandler(handler)
@app.route('/send',methods=["POST"])
def send():
    sms_type = 0
    appid="140016XXXXX"
    appkey="9993bac2a2b15aXXX"
    ssender = SmsSingleSender(appid, appkey)
    try:
        #print data['remobile'],data['text']
        result = ssender.send(sms_type, 86, '123',
            ['123'], extend="", ext="")
        print result
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

    print(result)
    return result

@app.route('/send_sms',methods=["POST"])

def send_sms():
    handler=logging.FileHandler('run.log',encoding='UTF-8')
    app.logger.addHandler(handler)
    succ={
            "status":0,
            "message":"发送成功"
        }
    fail={
            "status":1,
            "message":"发送失败" 
        }
    data=request.get_data()
    ip = request.remote_addr
    real_ip = request.http_x_forwarded_for
    zwdata=data.decode('UTF-8')
    print zwdata
    print ip
    app.logger.info("data:",zwdata)
    app.logger.info("ip:",ip)
    app.logger.info("real_ip:",real_ip)
    '''res=send()
    if res['result']==0:
        
        return succ
    else:
        
        return fail
'''
    print json.dumps(succ)
    return json.dumps(fail)


if __name__=='__main__':

	app.run(host='0.0.0.0',port=5001,debug=True)