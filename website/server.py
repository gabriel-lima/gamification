# encoding: utf-8
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/clientes', methods=['GET'])
def novo_evento():
    return render_template('clientes/novo.html')


if __name__ == '__main__':
    app.secret_key = '\xec\x84j\xcdY\xc7\xf7".\x0e\xf4o>\x0f\xc9\x88f\xf4svPG\xec\x8b'
    app.debug = True
    app.run()
    