from flask import Flask


application = Flask(__name__)
application.config['SECRET_KEY'] = 'd13ec20617d521687ae10b478342b8ad'

from application import routes
