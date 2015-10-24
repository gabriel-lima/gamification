# encoding: utf-8
from flask import Flask
from api import api
from web import web

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(web)


if __name__ == '__main__':
    app.secret_key = '\xec\x84j\xcdY\xc7\xf7".\x0e\xf4o>\x0f\xc9\x88f\xf4svPG\xec\x8b'
    app.debug = True
    app.run(port=5001)
