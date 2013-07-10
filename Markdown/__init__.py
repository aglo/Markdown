# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask.ext.misaka import Misaka
from flask import url_for
from flask import render_template, request, redirect, session
from flask import send_from_directory
from flask.ext.wtf import Form, TextAreaField, Length, TextField
from werkzeug import secure_filename

app = Flask(__name__)
Misaka(app)

from Markdown import default_settings
app.config.from_object(default_settings)

app.secret_key = app.config["SECRET_KEY"]

if not os.path.exists(app.config["DOWNLOAD_PATH"]):
    os.makedirs(app.config["DOWNLOAD_PATH"])

#
#load views
#
from Markdown import views
