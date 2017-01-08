import numpy as np
from train.learning.state import State

from train.learning.action import Actions


def state_and_actions_to_matrix(state: State, actions: Actions):
    return [state.to_list() + [action] for action in actions]


class QFunction(object):
    def __init__(self, model=None):
        self.model = model

    def evaluate(self, state: State, actions: Actions):
        matrix = state_and_actions_to_matrix(state, actions)
        return self.model.predict(matrix)

    def update_from_record(self, records):
        transitions = records.some_transitions(20)
        matrix = [transition.to_list() for transition in transitions]
        self.model.train(matrix)


class ZeroQFunction(object):
    def __init__(self):
        pass

    @staticmethod
    def evaluate(state: State, actions: Actions):
        return [0] * len(actions)


class RandomQFunction(object):
    def __init__(self):
        pass

    @staticmethod
    def evaluate(state: State, actions: Actions):
        return np.random.rand(len(actions))
