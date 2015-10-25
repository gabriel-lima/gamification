# coding: utf-8
import json
from flask import request, Response, Blueprint
from website import scene_gateway


api = Blueprint('api', __name__)


class GamifyCommand(object):
    def __init__(self):
        self.data = {}

    def command(self, name):
        if name == 'frete_gratis':
            self.data['script'] = '''
                humane.log('Legal! Adicione mais um produto e você ganhará o frete grátis.');
            '''


@api.route('/api/track', methods=['GET'])
def track():
    gamify = GamifyCommand()
    scenes = scene_gateway.all()

    for scene in scenes:
        if scene.script_python:
            event = request.args.get('event', None)
            exec scene.script_python

    jsonp = '%s(%s)' % (request.args.get('callback'), json.dumps(gamify.data))
    return Response(jsonp, content_type='text/javascript')