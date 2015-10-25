class SceneNotFoundException(Exception):
    pass


class SceneGatewayMemory(object):
    def __init__(self):
        self.records = []
        self.scene_id_increment = 0

    def save(self, scene):
        if scene.scene_id is None:
            self.scene_id_increment += 1
            scene.scene_id = self.scene_id_increment
        else:
            old_scene = self.get_by(scene.scene_id)
            self.records.remove(old_scene)
        self.records.append(scene)

    def get_by(self, scene_id):
        for record in self.records:
            if record.scene_id == scene_id:
                return record
        raise SceneNotFoundException()

    def all(self):
        return self.records
