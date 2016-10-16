from src.train.action import Actions


class Agent:
    def __init__(self, state=None, update_function=lambda s, a: s):
        self.state = state
        self.update_function = update_function

    def choose_best_action(self, actions):
        return actions[0]

    def update_state(self, action):
        self.state = self.update_function(self.state, action)

    def possible_actions(self):
        return Actions()
