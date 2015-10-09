# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, json, Response


app = Flask(__name__)


@app.route('/widget', methods=['GEt'])
def widget():
    callback = request.args.get('callback')

    html = 'Teste'
    script = '''
    <script>
    $(function () {
        humane.log('teste');
    });
    </script>
    '''
    css = '''
    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.1/css/materialize.min.css'>
    '''

    conteudo_em_json = json.dumps(
        {
            'html': html,
            'script': script,
            'css': css,
        })

    jsonp = '%s(%s)' % (callback, conteudo_em_json)
    return Response(jsonp, content_type='text/javascript')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/clientes/cadastrar', methods=['GET'])
def novo_cliente():
    return render_template('clientes/novo.html')


@app.route('/clientes/cadastrar', methods=['POST'])
def criar_cliente():
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
    app.run(port=5001)
