import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding
ACTION_TO_DIR = [
    # EAST
    np.array((1, 0)),
    # SOUTH
    np.array((0, 1)),
    # WEST
    np.array((-1, 0)),
    # NORTH
    np.array((0, -1)),
]
ACTION_SIZE = 4
GRID_SIZE = 5

class GridWorldEnv(gym.Env):
  metadata = {'render.modes': ['rgb_array']}
  current_pos = np.array((0,0))
  seed = None
  def __init__(self):
    self.action_space = spaces.Discrete(ACTION_SIZE)
    self.np_random, self.seed = seeding.np_random(self.seed)
    self.set_targets()
    self.reset()
  def set_targets(self, a=None,ap=None,b=None,bp=None):
    self.target_A_pos = a
    self.target_Ap_pos = ap
    self.target_B_pos = b
    self.target_Bp_pos = bp
    pass
  def step(self, action):
    dir_vec = ACTION_TO_DIR[action]
    new_pos = self.current_pos + dir_vec
    reward = 0
    if self.is_equal(self.target_A_pos,new_pos):
      reward = 10 
      self.current_pos = self.target_Ap_pos
    elif self.is_equal(self.target_B_pos,new_pos):
      reward = 5
      self.current_pos = self.target_Bp_pos
    elif self.is_outside(new_pos[0]) or self.is_outside(new_pos[1]):
      reward = -1
    else:
      self.current_pos = new_pos
    return [self.get_observations(), reward]
  def reset(self, new_targets=False):
    self.current_pos[0] = self.np_random.randint(GRID_SIZE)
    self.current_pos[1] = self.np_random.randint(GRID_SIZE)
    if self.target_A_pos is None or new_targets:
      self.target_A_pos = np.array((self.np_random.randint(GRID_SIZE),self.np_random.randint(GRID_SIZE)))
    if self.target_B_pos is None or new_targets:
      self.target_B_pos = np.array((self.np_random.randint(GRID_SIZE),self.np_random.randint(GRID_SIZE)))
    if self.target_Ap_pos is None or new_targets:
      self.target_Ap_pos = np.array((self.np_random.randint(GRID_SIZE),self.np_random.randint(GRID_SIZE)))
    if self.target_Bp_pos is None or new_targets:
      self.target_Bp_pos = np.array((self.np_random.randint(GRID_SIZE),self.np_random.randint(GRID_SIZE)))
    return [self.get_observations()]
  def render(self, mode='rgb_array', close=False):
    raise NotImplementedError
  def is_outside(self, index):
    return index >= GRID_SIZE or index < 0
  def is_equal(self, a,b):
    return a[0] == b[0] and a[1] == b[1]
  def get_observations(self):
    return {"current_pos": self.current_pos, "target_A_pos": self.target_A_pos, "target_B_pos": self.target_B_pos }
