from src.train.action import Actions
from src.train.state import State


def state_and_actions_to_matrix(state: State, actions: Actions):
    return [state.to_list() + [action] for action in actions]


class QFunction(object):
    def __init__(self, model=None):
        self.model = model

    def evaluate(self, state: State, actions: Actions):
        matrix = state_and_actions_to_matrix(state, actions)
        return self.model.predict(matrix)


class ZeroQFunction(object):
    def __init__(self):
        pass

    @staticmethod
    def evaluate(state: State, actions: Actions):
        return [0] * len(actions)
