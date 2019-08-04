import gym
import rl_salk
import numpy as np
env = gym.make('grid-world-v0')
a = np.array((1,0))
ap =np.array((1,4))
b =np.array((3,0))
bp = np.array((3,2))
env.set_targets(a,ap,b,bp)
[observation] = env.reset()
discount_factor = 0.9
learning_rate = 0.1
vs = np.zeros((5,5))
for i in range(1000):
    #eq policy
    action = env.action_space.sample()
    current_pos = observation["current_pos"]
    [observation, reward] = env.step(action)
    new_pos = observation["current_pos"]
    new_pos = observation["current_pos"]
    vsc = vs[current_pos[0], current_pos[1]]
    vsp = vsc - learning_rate * vsc
    vsn = vs[new_pos[0],new_pos[1]]
    vs[current_pos[0], current_pos[1]] = vsp + learning_rate*reward + discount_factor * learning_rate*vsn
    pass
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
print(np.rot90(vs,3))
