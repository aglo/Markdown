# -*- coding: utf-8 -*-
import sys
import os
from flask import Flask
from flask.ext.misaka import Misaka
from flask import url_for
from flask import render_template, request, redirect, session
from flask import send_from_directory
from flask.ext.wtf import Form, TextAreaField, Length, TextField
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'md'])
SECRET_KEY = 'development key'

app = Flask(__name__)
Misaka(app)
app.secret_key = SECRET_KEY

def decode_heuristically(string, enc = None, denc = sys.getdefaultencoding()):
    """
    Try to interpret 'string' using several possible encodings.
    @input : string, encode type.
    @output: a list [decoded_string, flag_decoded, encoding]
    """
    if isinstance(string, unicode):
        return string, 0, "utf-8"
    try:
        new_string = unicode(string, "ascii")
        return string, 0, "ascii"
    except UnicodeError:
        encodings = ["utf-8", "iso-8859-1", "cp1252", "iso-8859-15"]

        if denc != "ascii":
            encodings.insert(0, denc)
        if enc:
            encodings.insert(0, enc)

        for enc in encodings:
            if (enc in ("iso-8859-15", "iso-8859-1") and
                re.search(r"[\x80-\x9f]", string) is not None):
                continue
            if (enc in ("iso-8859-1", "cp1252") and
                re.search(r"[\xa4\xa6\xa8\xb4\xb8\xbc-\xbe]", string)\
                is not None):
                continue

            try:
                new_string = unicode(string, enc)
            except UnicodeError:
                pass
            else:
                if new_string.encode(enc) == string:
                    return new_string, 0, enc

    #If unable to decode,doing force decoding i.e.neglecting those chars.
    output = [(unicode(string, enc, "ignore"), enc) for enc in encodings]
    output = [(len(new_string[0]), new_string) for new_string in output]
    output.sort()
    new_string, enc = output[-1][1]
    return new_string, 1, enc

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
        file = request.files['uploadfile']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_content = decode_heuristically(file.stream.read(), "utf-8")[0]
            session['files'] = file_content
            session['filename'] = file.filename
            return redirect(url_for("markdown"))

    return render_template('upload.html')

@app.route('/markdown/download/', methods=['GET', 'POST'])
@app.route('/markdown/download', methods=['GET', 'POST'])
def download_file():
    class PostForm(Form):
        content = TextAreaField("content", validators=[Length(min=1, message="Not Null")])
        title = TextField("title", validators=[Length(min=1, message="Not Null")])

    DOWNLOAD_PATH = "~/MarkdownOnline/download"

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
