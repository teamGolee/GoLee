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
        r = db.getWork(url)

    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

