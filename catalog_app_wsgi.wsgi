#!/usr/bin python
import sys
sys.path.insert(0,"/var/www/app_wsgi")

from catalog_app import app as application
application.secret_key = 'Make a new secret key'

