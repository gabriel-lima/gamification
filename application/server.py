from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.secret_key = ')\xe8\xd3\x1e\xf3\x06$\x9ct\xb4\xcc$3\xd6\xf6/St\xd9\xad(\xe4h1'
    app.debug = True
    app.run()