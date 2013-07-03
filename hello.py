# -*- coding: utf-8 -*-
import sys
import os
from flask import Flask
from flask.ext.misaka import Misaka
from flask import url_for
from flask import render_template, request, redirect, session, send_from_directory
from flask.ext.wtf import Form, TextAreaField, Length, TextField
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/arkfang/flaskproject/upload'
ALLOWED_EXTENSIONS = set(['txt', 'md'])
SECRET_KEY = 'development key'

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
Misaka(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index/')
def index():
    return render_template('hello.html')

@app.route('/markdown/', methods=['GET', 'POST'])
@app.route('/markdown', methods=['GET', 'POST'])
def markdown():
    class PostForm(Form):
        content = TextAreaField("content", validators=[Length(min=1, message="Not Null")])
        title = TextField("title", validators=[Length(min=1, message="Not Null")])

    form = PostForm(csrf_enabled=False)

    if 'files' and 'filename' in session:
        form.content.data = session.pop('files', None)
        form.title.data = session.pop('filename', None)
    return render_template('markdown.html', form=form)

@app.route('/markdown/upload/', methods=['GET', 'POST'])
@app.route('/markdown/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print "why kidding me!"
        file = request.files['uploadfile']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            session['files'] = file.stream.read()
            session['filename'] = file.filename
            return redirect(url_for("markdown"))

    return render_template('upload.html')

@app.route('/markdown/download/', methods=['GET', 'POST'])
@app.route('/markdown/download', methods=['GET', 'POST'])
def download_file():
    class PostForm(Form):
        content = TextAreaField("content", validators=[Length(min=1, message="Not Null")])
        title = TextField("title", validators=[Length(min=1, message="Not Null")])

    DOWNLOAD_PATH = "upload"

    form = PostForm(csrf_enabled=False)

    if form.content.data:
        filename = form.title.data
        path = ""
        if not filename.endswith(".md"):
            filename = filename + ".md"

        path = DOWNLOAD_PATH + "/" + filename
        path = path.encode("utf-8")
        f = file(path, "w+")
        f.write(form.content.data)
        f.close()

    return send_from_directory(DOWNLOAD_PATH, filename, as_attachment=True)

if __name__ == '__main__':
#    app.run(host='0.0.0.0')
    app.run(debug=True)
