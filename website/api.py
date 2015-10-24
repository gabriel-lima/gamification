# encoding: utf-8
import json
from flask import request, Response, Blueprint


api = Blueprint('api', __name__)


@api.route('/api/track', methods=['GET'])
def track():

    data = {}
    data['success'] = True

    data['script'] = '''
        humane.log('<img height="80px" width="80px" src="https://cdn4.iconfinder.com/data/icons/flaten/512/award-512.png">Parabéns! <b>+1 ponto</b>');
    '''

    jsonp = '%s(%s)' % (request.args.get('callback'), json.dumps(data))
    return Response(jsonp, content_type='text/javascript')