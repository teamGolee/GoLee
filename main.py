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

    if db.getWork(url) == 'None':
        print('LogPoint4')
        db.postWork(url)
        r = db.getWork(url)

    else:
        r = db.getWork(url)

    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
