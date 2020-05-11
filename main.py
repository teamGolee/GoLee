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

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post", methods=['POST'])
def post():
    value = request.form['test']
    s = SafeBrowsing(os.getenv('gsb_key'))
    r = s.lookup_urls(['{}'.format(value)])

    return r

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
