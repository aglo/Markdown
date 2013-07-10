# -*- coding: utf-8 -*-
import os

from flask import send_from_directory, redirect, url_for, request, jsonify
from flask.ext.wtf import Form, TextField, TextAreaField, Length
from Markdown import app
from Markdown import default_settings

@app.route('/download/', methods=['GET', 'POST'])
@app.route('/download', methods=['GET', 'POST'])
def download():

    title = request.form["title"]
    content = request.form["content"]

    if content:
        filename = title
        path = ""
        if not filename.endswith(".md"):
            filename = filename + ".md"

        path = app.config["DOWNLOAD_PATH"] + "/" + filename
        path = path.encode("utf-8")
        f = file(path, "w+")
        f.write(content)
        f.close()
        return send_from_directory(app.config["DOWNLOAD_PATH"], filename, as_attachment=True)

    return redirect(url_for("markdown"))
