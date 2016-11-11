from random import random, choice

import numpy as np

from train.action import Actions
from train.q_function import ZeroQFunction


def state_to_empty_actions(state):
    return Actions()


class Agent:
    def __init__(self, state=None, q_function=None,
                 state_to_actions_function=state_to_empty_actions):
        """
        An agent is the object moving or acting in your experiment. It has a
        state and a q_function, which, given a state and some actions, evaluate
        the value of each actions. The possible states accessible from a given
        state is computed by the state_to_action_function.
        :param state:
        :param q_function:
        :param state_to_actions_function:
        """
        self.state = state
        self.q_function = q_function if q_function is not None \
            else ZeroQFunction()
        self.state_to_actions_function = state_to_actions_function

    def choose_best_action(self, actions):
        q_values = self.q_function.evaluate(self.state, actions)
        return actions[np.argmax(q_values)]

    def update_state(self, action):
        self.state = self.state.update(action)

    def possible_actions(self):
        return self.state_to_actions_function(self.state)

    def set_state(self, state):
        return Agent(state, self.q_function, self.state_to_actions_function)


# noinspection PyMissingConstructor
class ExploratoryAgent(Agent):
    def __init__(self, agent: Agent, epsilon=0.1):
        self.agent = agent
        self.epsilon = epsilon

    def choose_best_action(self, actions):
        test = random()
        if test < self.epsilon:
            return choice(actions)
        else:
            return self.agent.choose_best_action(actions)

    def update_state(self, action):
        self.agent.update_state(action)

    def possible_actions(self):
        return self.agent.possible_actions()

    def set_state(self, state):
        return ExploratoryAgent(self.agent.set_state(state), self.epsilon)

    @property
    def state(self):
        return self.agent.state
