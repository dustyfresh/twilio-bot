from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .sms import *
from .call import *
