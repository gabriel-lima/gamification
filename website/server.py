# encoding: utf-8
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/eventos', methods=['GET'])
def novo_evento():
    return render_template('eventos/novo.html')


@app.route('/cenarios', methods=['GET'])
def novo_cenario():
    return render_template('cenarios/novo.html')


if __name__ == '__main__':
    app.secret_key = ')\xe8\xd3\x1e\xf3\x06$\x9ct\xb4\xcc$3\xd6\xf6/St\xd9\xad(\xe4h1'
    app.debug = True
    app.run()
    