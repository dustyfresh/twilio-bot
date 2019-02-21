from . import routes
from flask import request, session, redirect

'''
	Index route
'''
@routes.route('/', methods=['GET'])
def index():
	return 'denied', 403
