class Engine(object):
    def __init__(self, script):
        self.script = script

    def execute(self, gamify, event):
        if self.script:
            exec self.script
