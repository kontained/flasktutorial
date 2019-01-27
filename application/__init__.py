from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd13ec20617d521687ae10b478342b8ad'

from application import routes
