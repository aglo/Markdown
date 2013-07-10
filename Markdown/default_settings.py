# -*- coding: utf-8 -*-
import os

#
#flask secret key
#
SECRET_KEY = "develop key"

#
#Path for Download files stored
#
DOWNLOAD_PATH = os.path.expanduser('~') + "/MarkdownOnline/download"

#
#Upload Files type check
#
ALLOWED_EXTENSIONS = set(['txt', 'md'])
