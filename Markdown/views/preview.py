# -*- coding: utf-8 -*-

from flask import jsonify, request
from Markdown import app
from flask.ext.misaka import markdown

@app.route('/preview', methods=['GET', 'POST'])
def preview():
    text = request.form["text"]
    return jsonify(text=markdown(text))
