import gym
import test_env as e

from random import random
'''
import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self, n_observations: int, n_actions: int) -> None:
        super(DQN, self).__init__()
        self.layer1 = nn.Linear(n_observations, 128)
        self.layer2 = nn.Linear(128, 128)
        self.layer3 = nn.Linear(128, n_actions)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        return self.layer3(x)
'''

class BatiScheduler():
    def act(self, obs):
        pass

    def play(self, env, verbose=True):
        pass

def run():
    agent = BatiScheduler()
    env   = gym.make()

    hist  = agent.play(env, True)
    print("[DONE]")
