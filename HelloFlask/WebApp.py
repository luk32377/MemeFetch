#!/usr/bin/python

from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route("index"
def index():
	return render_template

if __name__ = "__main__":
	app.run()