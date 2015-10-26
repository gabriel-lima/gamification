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
                humane.log('Legal! Adicione mais um produto e você ganhará o frete grátis.', function() { callback(); });
            '''
        if name == 'cupom_desconto':
            self.data['script'] = '''
                humane.log('Parabéns! Você acaba de ganhar um cupom de desconto para a sua próxima compra.', function() { callback(); });
            '''


class Engine(object):
    def __init__(self, script):
        self.script = script

    def execute(self, gamify, event):
        if self.script:
            exec self.script


@api.route('/api/track', methods=['GET'])
def track():
    event = request.args.get('event', None)

    gamify = GamifyCommand()

    scenes = scene_gateway.all()
    for scene in scenes:
        engine = Engine(scene.script_python)
        engine.execute(gamify, event)

    jsonp = '%s(%s)' % (request.args.get('callback'), json.dumps(gamify.data))
    return Response(jsonp, content_type='text/javascript')
