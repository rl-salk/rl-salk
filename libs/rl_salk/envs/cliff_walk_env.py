import gym
import numpy as np
from gym import spaces
from gym.utils import seeding

ACTION_TO_DELTA = [
    np.array((1, 0)),   # EAST
    np.array((0, 1)),   # SOUTH
    np.array((-1, 0)),  # WEST
    np.array((0, -1)),  # NORTH
]
NUM_ACTIONS = len(ACTION_TO_DELTA)


class CliffWalkEnv(gym.Env):

    seed = None

    def __init__(self, grid_size=(12, 4), cliff_penalty=-100):

        self.np_random, self.seed = seeding.np_random(self.seed)
        self.action_space = spaces.Discrete(NUM_ACTIONS)

        self.cliff_penalty = cliff_penalty

        self.grid_size = np.array(grid_size)
        self.start_pos = np.array((0, self.grid_size[1] - 1))
        self.goal_pos = self.grid_size - 1
        self.current_pos = None

    def reset(self):
        self.set_pos(self.start_pos)
        obs = self.get_observation()
        return obs

    def set_pos(self, pos):
        self.current_pos = pos.copy()

    def step(self, action):
        delta = ACTION_TO_DELTA[action]
        new_pos = self.current_pos + delta

        reward = -1
        done = False

        if self.in_bounds(new_pos):  # in bounds

            if self.at_goal(new_pos):  # at goal
                self.set_pos(new_pos)
                done = True

            elif self.on_cliff(new_pos):  # on cliff
                self.set_pos(self.start_pos)
                reward = self.cliff_penalty

            else:  # in bounds, not at goal or on cliff
                self.set_pos(new_pos)

        else:  # out of bounds
            pass  # don't update pos

        obs = self.get_observation()
        info = {}
        return [obs, reward, done, info]

    def on_cliff(self, pos):
        on_bottom = (pos[1] == self.grid_size[1] - 1)
        on_sides = (pos[0] == 0) or (pos[0] == self.grid_size[0] - 1)
        return on_bottom and not on_sides

    def at_goal(self, pos):
        return pos_equal(pos, self.goal_pos)

    def in_bounds(self, pos):
        return np.logical_and(pos >= 0, pos < self.grid_size)

    def get_observation(self):
        obs = {"current_pos": self.current_pos}
        return obs

    def render(self, mode='rgb_array', close=False):
        raise NotImplementedError


def pos_equal(pos1, pos2):
    eq = (pos1 == pos2).all()
    return eq
