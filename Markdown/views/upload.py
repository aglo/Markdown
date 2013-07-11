# -*- coding: utf-8 -*-
from markdown2 import markdown
import pygments

from flask import redirect, render_template, session, request, url_for
from werkzeug import secure_filename
from Markdown import app
from flask import jsonify
from Markdown.models.decode_heuristically import decode_heuristically

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config["ALLOWED_EXTENSIONS"]

@app.route('/upload/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        file = request.files['uploadfile']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_content = decode_heuristically(file.stream.read(), "utf-8")[0]
            return jsonify(text=markdown(file_content,
                                         extras=['fenced-code-blocks',
                                                 'code-color']),
                           title=filename,
                           content=file_content)

    return render_template('upload.html')
