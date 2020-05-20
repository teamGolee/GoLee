import sys
import json
import logging
import time
import urllib
import os

from flask import Flask
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from pysafebrowsing import SafeBrowsing
from urllib import parse
from restfulmodel import RestfulModelling
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
        r = db.getWork(url)

    return r


if __name__ == "__main__":
    # 현제 로컬에서 작업중이므로 5000 , 포트는 유동적변경
    app.run(host="0.0.0.0", debug=True, port=5000)
