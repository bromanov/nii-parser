#!/usr/bin python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template
import redis

app = Flask(__name__)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/')
def hello_world():
    return render_template("hello.html")

@app.route('/api/signup/<username>')
def save_user_email(username):
    r.set(username, username)
    print "saved email %s" % username
    return "ok"

if __name__ == '__main__':
    app.debug = True
    app.run()