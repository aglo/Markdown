# -*- coding: utf-8 -*-
import os
import misaka

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


#
#misaka defualt settings
#
EXTENSIONS = misaka.EXT_NO_INTRA_EMPHASIS | \
  misaka.EXT_TABLES | \
  misaka.EXT_FENCED_CODE | \
  misaka.EXT_AUTOLINK | \
  misaka.EXT_STRIKETHROUGH | \
  misaka.EXT_LAX_HTML_BLOCKS | \
  misaka.EXT_SPACE_HEADERS | \
  misaka.EXT_SUPERSCRIPT
