'''trpdtrails Application Entry Point'''
from flask import Flask
app = Flask(__name__)

import trpdtrails.routes
