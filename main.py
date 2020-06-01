import datetime
import json
import logging
import os
import sys
import time
import urllib

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from pysafebrowsing import SafeBrowsing
from restfulmodel import RestfulModelling
from urllib import parse


app = Flask(__name__)


@app.route("/")
def index():

    return render_template('index.html')


# Post 요청
@app.route("/post", methods=['POST'])
def post():

    db = RestfulModelling()
    url = request.get_json()

    # 조회해서 데이터가 비어있으면 포스트 요청을 한 후 다시 값을 받아옴
    if db.getWork(url) == 'None':
        db.postWork(url)
        r = db.getWork(url)
    else:

        #
        ##30일 이상 업데이트가 없으면 업데이트
        #
        r = db.getWork(url)
        dbupdatetime = r['update_time']
        dbtime = r['insert_time']
        tempurl = r
        now = time.localtime()
        d = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon,
                                               now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        nowtime = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        #
        ## 한번도 업데이트가 없을 경우
        #
        if dbupdatetime == None:
            if (dbtime+datetime.timedelta(days=30)) < nowtime:
                db.updateWork(nowtime, tempurl)
                r = db.getWork(url)
        
        elif dbupdatetime != None:
            if (dbupdatetime+datetime.timedelta(days=30)) < dbupdatetime:
                db.updateWork(nowtime, tempurl)
                r = db.getWork(url)

    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
