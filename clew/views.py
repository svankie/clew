__author__ = 'svankiE'

from clew import app

@app.route('/', methods=['GET'])
def index():
    return "ayyy ay ay!"