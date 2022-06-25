#!/home/xs017738/venaqui.net/public_html/https://test.venaqui.net/venaqui/python3
# encoding: utf-8

import sys, os

sys.path.append("/home/xs017738/venaqui.net/public_html/test.venaqui.net/venaqui/")

os.environ['DJANGO_SETTINGS_MODULE'] = "venaqui.settings"

from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)