# -*- coding: utf-8 -*-
import pygments
from markdown2 import markdown

from flask import jsonify, request
from Markdown import app

@app.route('/preview', methods=['GET', 'POST'])
def preview():
    text = request.form["text"]
    return jsonify(text=markdown(text, extras=['fenced-code-blocks', 'code-color']))
