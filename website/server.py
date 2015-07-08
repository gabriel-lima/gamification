# encoding: utf-8
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/clientes/cadastrar', methods=['GET'])
def novo_cliente():
    return render_template('clientes/novo.html')


@app.route('/clientes', methods=['GET'])
def lista_de_clientes():
    return render_template('clientes/lista.html')


if __name__ == '__main__':
    app.secret_key = '\xec\x84j\xcdY\xc7\xf7".\x0e\xf4o>\x0f\xc9\x88f\xf4svPG\xec\x8b'
    app.debug = True
    app.run()
    