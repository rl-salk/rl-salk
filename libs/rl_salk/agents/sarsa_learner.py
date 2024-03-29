from rl_salk.agents.td_learner import TDLearner


class SarsaLearner(TDLearner):

    def learn(self, prev_state, action, state, reward, done):
        super().learn(prev_state, action, state, reward, done,
                      target_policy='behavior')
