from random import random, choice

from src.train.action import Actions


def state_to_empty_actions(state):
    return Actions()


class Agent:
    def __init__(self, state=None, update_state_function=lambda s, a: s,
                 state_to_action_function=state_to_empty_actions):
        self.state = state
        self.update_state_function = update_state_function
        self.state_to_actions_function = state_to_action_function

    def choose_best_action(self, actions):
        return actions[0]

    def update_state(self, action):
        self.state = self.update_state_function(self.state, action)

    def possible_actions(self):
        return self.state_to_actions_function(self.state)


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
