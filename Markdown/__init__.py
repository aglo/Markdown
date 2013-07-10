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

#
#load views
#
from Markdown import views
