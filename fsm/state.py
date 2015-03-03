class State(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(State, self).__new__(self)
        return self._instance
    def enter(self):
        pass
    def execute(self):
        pass
    def exit(self):
        pass