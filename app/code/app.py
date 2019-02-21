#!/usr/bin/env python
from flask import Flask
from routes import *
from base64 import b64encode
import json
import os
import datetime

application = Flask(__name__)

# Session lifetime set to 48 hours by default
# http://flask.pocoo.org/docs/0.12/config/#configuration-basics
application.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=48)

# secret_key is explained here:
# http://flask.pocoo.org/docs/1.0/quickstart/#sessions
application.secret_key = b64encode(os.urandom(255))[:255]

# We organize all of our routes in the /opt/app/routes directory
application.register_blueprint(routes)

# Apply these headers after each request
@application.after_request
def after_request(response):
	response.headers['Server'] = '' # override nginx's server banner
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '0'
	response.headers['Cache-Control'] = 'public, max-age=0'
	response.headers['X-XSS-Protection'] = '1; mode=block'
	response.headers['Strict-Transport-Security'] = 'max-age=86400; includeSubDomains'
	return response

if __name__ == '__main__':
	application.run(
		host='127.0.0.1',
		port=8080,
		threaded=True,
	)
