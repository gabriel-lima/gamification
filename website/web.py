import json

from flask import render_template, Blueprint, request, Response, redirect, url_for

from website import scene_gateway
from core import SceneStruct
from gateways import SceneNotFoundException


web = Blueprint('web', __name__)


from storage import populate_storage
populate_storage()


@web.route('/')
def index():
    return render_template('base.html')


@web.route('/scene/create', methods=['POST'])
def create_scene():
    scene = SceneStruct(name=request.form['scene_name'],
                        description=request.form['scene_description'])
    scene_gateway.save(scene)
    return redirect(url_for('web.edit_scene', scene_id=scene.scene_id))


@web.route('/scene/<int:scene_id>', methods=['GET'])
def edit_scene(scene_id):
    scene = scene_gateway.get_by(scene_id)
    return render_template('scenes/edit.html', scene=scene)


@web.route('/scene/delete/<int:scene_id>', methods=['GET'])
def delete_scene(scene_id):
    scene_gateway.delete(scene_id)
    return redirect(url_for('web.list_scenes'))


@web.route('/scene/clone/<int:scene_id>', methods=['GET'])
def clone_scene(scene_id):
    scene = scene_gateway.get_by(scene_id)
    scene.scene_id = None
    scene_gateway.save(scene)
    return redirect(url_for('web.list_scenes'))


@web.route('/scenes', methods=['GET'])
def list_scenes():
    scenes = scene_gateway.all()
    return render_template('scenes/list.html', scenes=scenes)


@web.route('/scene/xml/load/<int:scene_id>', methods=['GET'])
def load_xml_scene(scene_id):
    scene = scene_gateway.get_by(scene_id)
    return Response(scene.storage_xml, content_type='text/xml')


@web.route('/scene/xml/save', methods=['POST'])
@web.route('/scene/xml/save/<int:scene_id>', methods=['POST'])
def save_xml_scene(scene_id=None):
    try:
        scene = scene_gateway.get_by(scene_id)
    except SceneNotFoundException:
        scene = SceneStruct()

    scene.storage_xml = request.data
    scene_gateway.save(scene)

    return Response(json.dumps({'scene_id': scene.scene_id}), content_type='application/json')


@web.route('/scene/python/save/<int:scene_id>', methods=['POST'])
def save_python_scene(scene_id):
    scene = scene_gateway.get_by(scene_id)
    scene.script_python = request.data
    scene_gateway.save(scene)

    return Response()

