# -*- coding: utf-8 -*-
from flask import redirect, render_template, session, request, url_for
from werkzeug import secure_filename
from Markdown import app
from Markdown.models.decode_heuristically import decode_heuristically

ALLOWED_EXTENSIONS = set(['txt', 'md'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/markdown/upload/', methods=['GET', 'POST'])
@app.route('/markdown/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['uploadfile']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_content = decode_heuristically(file.stream.read(), "utf-8")[0]
            session['files'] = file_content
            session['filename'] = file.filename
            return redirect(url_for("markdown"))

    return render_template('upload.html')
