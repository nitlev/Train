class Actions:
    def __init__(self, *args):
        self.actions = list(args)

    def is_empty(self):
        return len(self.actions) == 0

    def __getitem__(self, item):
        return self.actions[item]
