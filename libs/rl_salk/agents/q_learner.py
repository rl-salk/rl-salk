from gym.utils import seeding
import numpy as np


class QLearner(object):

    def __init__(self, n_states, n_actions, epsilon=0.1, gamma=0.99,
                 alpha=0.1):

        self.np_random, self.seed = seeding.np_random(None)

        self.epsilon = epsilon
        self.gamma = gamma
        self.alpha = alpha

        self.n_states = n_states
        self.n_actions = n_actions

        self.init_q()

    def init_q(self):
        self.q = np.zeros((self.n_states, self.n_actions))

    def reset(self, state):
        pass

    def sample_action(self, state):
        if self.np_random.rand() < self.epsilon:
            action = self.np_random.randint(0, self.n_actions)  # random action
        else:
            action = np.argmax(self.q[state])  # greedy action
        return action

    def learn(self, prev_state, action, state, reward, done):
        (s, a, s_, r) = (prev_state, action, state, reward)
        # TD update
        self.q[s, a] = (self.q[s, a]
                        + self.alpha * (r
                                        + self.gamma * np.max(self.q[s_])
                                        - self.q[s, a]))
