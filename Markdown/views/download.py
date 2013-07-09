# -*- coding: utf-8 -*-
import os

from flask import send_from_directory, redirect, url_for
from flask.ext.wtf import Form, TextField, TextAreaField, Length
from Markdown import app
from Markdown import default_settings

@app.route('/markdown/download/', methods=['GET', 'POST'])
@app.route('/markdown/download', methods=['GET', 'POST'])
def download_file():
    class PostForm(Form):
        content = TextAreaField("content", validators=[Length(min=1, message="Not Null")])
        title = TextField("title", validators=[Length(min=1, message="Not Null")])

    form = PostForm(csrf_enabled=False)

    if form.content.data:
        filename = form.title.data
        path = ""
        if not filename.endswith(".md"):
            filename = filename + ".md"

        path = app.config["DOWNLOAD_PATH"] + "/" + filename
        path = path.encode("utf-8")
        f = file(path, "w+")
        f.write(form.content.data)
        f.close()
        return send_from_directory(app.config["DOWNLOAD_PATH"], filename, as_attachment=True)

    return redirect(url_for("markdown"))
