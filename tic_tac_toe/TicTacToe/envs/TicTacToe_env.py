import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
BOX_SIZE = [3,3]

class TicTacToeEnv(gym.Env):
    metadata = {'render.modes': ['human']}    
    #current_state = np.array(BOX_SIZE[0],BOX_SIZE[1]) 
    def __init__(self):
        #self.action_space = spaces.Discrete(ACTION_SIZE)
        #self.observation_space = spaces.Box(3,3)#(BOX_SIZE[0],BOX_SIZE[1])
        self.np_random, self.seed = seeding.np_random(self.seed)
        self.current_state = np.array(BOX_SIZE[0],BOX_SIZE[1])

    def step(self, action):
        done = False
        #current_state = self.observation_space
        options = np.where(self.current_state == 0)
        self.current_state[options[self.seed]] = 1
        if (self.current_state[0,:] == 1) or (self.current_state[1,:] == 1) or\
            (self.current_state[2,:] == 1) or (self.current_state [:,0] == 1) or\
            (self.current_state[:,1] == 1) or (self.current_state [:,2] == 1) or\
            (self.current_state[0,0] == self.current_state[1,1] == self.current_state[2,2] == 1) or\
            (self.current_state[0,2] == self.current_state[1,1] == self.current_state[2,0] == 1):
            reward = 1
            done = True
        elif (self.current_state[0,:] == 2) or (self.current_state[1,:] == 2) or\
            (self.current_state[2,:] == 2) or (self.current_state [:,0] == 2) or\
            (self.current_state[:,1] == 2) or (self.current_state [:,2] == 2) or\
            (self.current_state[0,0] == self.current_state[1,1] == self.current_state[2,2] == 2) or\
            (self.current_state[0,2] == self.current_state[1,1] == self.current_state[2,0] == 2): 
            reward = -1
            done = True
        elif (len(np.where(self.current_state==0)[0])==0:
            reward = -1
            done = True
        else:
            reward = 0 
        if done:
            self.reset()
        return(self.current_state, reward, done)  

    def reset(self):
        self.current_state = np.zeros(BOX_SIZE[0],BOX_SIZE[1])
        return self.current_state


    def render(self, mode='human', close=False):
        raise NotImplementedError
            