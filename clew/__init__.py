__author__ = 'svankiE'

from flask import Flask
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:hor4cio@localhost:5432/clew-dev"

import clew.views