from gym.envs.registration import register

register(
    id='grid-world-v0',
    entry_point='rl_salk.envs:GridWorldEnv',
)

register(
    id='cliff-walk-v0',
    entry_point='rl_salk.envs:CliffWalkEnv',
)
