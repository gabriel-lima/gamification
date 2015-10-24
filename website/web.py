# encoding: utf-8
from flask import render_template, Blueprint


web = Blueprint('web', __name__)


@web.route('/')
def index():
    return render_template('base.html')