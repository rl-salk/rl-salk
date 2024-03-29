"""
TDLearner is an agent that implements different Temporal Difference (TD)
learning algorithms from Sutton & Barto, Ch 3, pages 130-131.

QLearner and SarsaLearner are subclasses of TDLearner.

Usage:

env = gym.make('cliff-walk-v0')
agent = QLearner(n_states, n_actions, epsilon=0.1, gamma=1.0, alpha=0.1)
obs = env.reset()
for _ in range(1000):
    action = agent.sample_action(state)
    (obs_, reward, done, info) = env.step(action)
    agent.learn(obs, action, obs_, reward, done)
    obs = obs_

"""

from gym.utils import seeding
import numpy as np


class TDLearner(object):

    def __init__(self, n_states, n_actions, exploration_prob=0.1,
                 discount_rate=0.99, learning_rate=0.1):

        self.np_random, self.seed = seeding.np_random(None)

        self.exploration_prob = exploration_prob
        self.discount_rate = discount_rate
        self.learning_rate = learning_rate

        self.n_states = n_states
        self.n_actions = n_actions

        self.init_q()

    def init_q(self):
        self.q = np.zeros((self.n_states, self.n_actions))

    def reset(self, state):
        pass

    def sample_action(self, state):
        if self.np_random.rand() < self.exploration_prob:
            action = self.np_random.randint(0, self.n_actions)  # random action
        else:
            action_values = self.q[state, :]
            action = np.argmax(action_values)  # greedy action
        return action

    def learn(self, prev_state, action, state, reward, done,
              target_policy='optimal'):

        (s, a, s_, r) = (prev_state, action, state, reward)

        action_values = self.q[s_, :]
        if target_policy == 'optimal':
            # Q-Learning (Sutton & Barto, p. 131)
            value = np.max(action_values)
        elif target_policy == 'behavior':
            # SARSA (Sutton & Barto, p. 130)
            a_ = self.sample_action(s_)
            value = action_values[a_]
        else:
            raise Exception(('target_policy value "{}"'
                             'not recognized').format(target_policy))

        # TD update
        self.q[s, a] = (self.q[s, a]
                        + self.learning_rate * (r + self.discount_rate * value
                                                - self.q[s, a]))
