# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.misaka import Misaka
from flask import url_for
from flask import render_template, request, redirect, session
from flask import send_from_directory
from flask.ext.wtf import Form, TextAreaField, Length, TextField
from werkzeug import secure_filename

SECRET_KEY = 'development key'
DOWNLOAD_PATH = "~/markdownOnline/download"

app = Flask(__name__)
Misaka(app)
app.secret_key = SECRET_KEY

#
#load views
#
from Markdown import views
