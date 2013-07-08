# -*- coding: utf-8 -*-
from flask import render_template, session
from flask.ext.wtf import Form, TextField, TextAreaField, Length
from Markdown import app

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
