from src.train.action import Actions


def state_to_empty_actions(state):
    return Actions()


class Agent:
    def __init__(self, state=None, update_function=lambda s, a: s,
                 state_to_action_function=state_to_empty_actions):
        self.state = state
        self.update_function = update_function
        self.state_to_actions_function = state_to_action_function

    def choose_best_action(self, actions):
        return actions[0]

    def update_state(self, action):
        self.state = self.update_function(self.state, action)

    def possible_actions(self):
        return self.state_to_actions_function(self.state)
