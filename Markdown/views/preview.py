# -*- coding: utf-8 -*-

from flask import jsonify, request
from Markdown import app
from Markdown.models.markdown import BleepRenderer

import misaka

@app.route('/preview', methods=['GET', 'POST'])
def preview():

    renderer = BleepRenderer()

    md = misaka.Markdown(renderer,
                         extensions=misaka.EXT_FENCED_CODE |
                         misaka.EXT_NO_INTRA_EMPHASIS)
    text = request.form["text"]
    return jsonify(text=md.render(text))
