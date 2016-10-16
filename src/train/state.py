class State:
    def __init__(self, *args):
        self.args = args

    def to_list(self):
        return list(self.args)
