# coding: utf-8
import json
from flask import render_template, Blueprint, request, Response
from website import scene_gateway
from scene_struct import SceneStruct
from website.scene_gateway_memory import SceneNotFoundException


web = Blueprint('web', __name__)


@web.route('/')
def index():
    return render_template('base.html')


@web.route('/scene/new', methods=['GET'])
def new_scene():
    return render_template('scenes/new.html')


@web.route('/scene/<int:scene_id>', methods=['GET'])
def edit_scene(scene_id):
    return render_template('scenes/edit.html', scene_id=scene_id)


@web.route('/scene/xml/load/<int:scene_id>', methods=['GET'])
def load_xml_scene(scene_id):
    scene = scene_gateway.get_by(scene_id)
    return Response(scene.format_xml, content_type='text/xml')


@web.route('/scene/xml/save', methods=['POST'])
@web.route('/scene/xml/save/<int:scene_id>', methods=['POST'])
def save_xml_scene(scene_id=None):
    try:
        scene = scene_gateway.get_by(scene_id)
    except SceneNotFoundException:
        scene = SceneStruct()

    scene.format_xml = request.data
    scene_gateway.save(scene)

    return Response(json.dumps({'scene_id': scene.scene_id}), content_type='application/json')


@web.route('/scene/python/save/<int:scene_id>', methods=['POST'])
def save_python_scene(scene_id):
    scene = scene_gateway.get_by(scene_id)
    scene.script_python = request.data
    scene_gateway.save(scene)

    return Response()

