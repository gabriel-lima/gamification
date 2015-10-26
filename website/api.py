import json
from flask import request, Response, Blueprint
from website import scene_gateway
from core import Engine
from core import GamifyCommand


api = Blueprint('api', __name__)


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
