#!/usr/bin/env python
import sys
sys.path.insert(0,"/vagrant")
# sys.path.insert(0,'/var/www/catalog-db')
# sys.path.insert(0,'/var/www/catalog-db/catalog-db')

from catalog_app import app as application
application.secret_key = 'Make a new secret key'

