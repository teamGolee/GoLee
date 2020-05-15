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
    print(render_template('index.html'))
    return render_template('index.html')


@app.route("/post", methods=['POST'])
def post():
    db = RestfulModelling()
    url = request.get_json()
    print(url)
    print(db.getWork(url))
    if db.getWork(url) == None:
        print('디비에 있긴한데')

    else:
        print('데이터가없어서 보내긴했어 ')
        db.postWork(url)

    s = SafeBrowsing('a')
    print(url)
    r = s.lookup_urls(['{}'.format(url['url'])])
    print(type(r))
    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
