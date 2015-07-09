# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for

# import pdb


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/clientes/cadastrar', methods=['GET'])
def novo_cliente():
    return render_template('clientes/novo.html')


@app.route('/clientes/cadastrar', methods=['POST'])
def criar_cliente():
    # pdb.set_trace()
    print request.form['nome']
    print request.form['sobrenome']
    print request.form['email']
    print request.form['telefone']
    print request.form['tipo_pessoa']
    # print request.form['data_nascimento']
    print request.form['observacoes']

    return redirect(url_for('lista_de_clientes'))


@app.route('/clientes', methods=['GET'])
def lista_de_clientes():
    return render_template('clientes/lista.html')


if __name__ == '__main__':
    app.secret_key = '\xec\x84j\xcdY\xc7\xf7".\x0e\xf4o>\x0f\xc9\x88f\xf4svPG\xec\x8b'
    app.debug = True
    app.run()
