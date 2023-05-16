#Adapted from
#[Christianos et al., 2020] Filippos Christianos, Lukas
#Sch ̈afer, and Stefano V Albrecht. Shared experience
#actor-critic for multi-agent reinforcement learning. In
#Thirty-fourth Conference on Neural Information Process-
#ing Systems, pages 10707–10717. Curran Associates Inc,
#2020
#Orginal code location: https://github.com/semitable/seac

import math

import torch
import torch.nn as nn
import torch.nn.functional as F

from utils import init

"""
Modify standard PyTorch distributions so they are compatible with this code.
"""
# Categorical
class FixedCategorical(torch.distributions.Categorical):
    def sample(self):
        newProbs = [i * 100 for i in self.probs] #For Exp
        return super().sample().unsqueeze(-1), newProbs  #For Exp
        #return super().sample().unsqueeze(-1) #for train and evaluate

    def log_probs(self, actions):
        return (
            super()
            .log_prob(actions.squeeze(-1))
            .view(actions.size(0), -1)
            .sum(-1)
            .unsqueeze(-1)
        )

    def mode(self):
        newProbs = [i * 100 for i in self.probs] #For Exp
        return self.probs.argmax(dim=-1, keepdim=True), newProbs  #For Exp
        #return self.probs.argmax(dim=-1, keepdim=True) #For train and evalate


class Categorical(nn.Module):
    def __init__(self, num_inputs, num_outputs):
        super(Categorical, self).__init__()

        init_ = lambda m: init(
            m, nn.init.orthogonal_, lambda x: nn.init.constant_(x, 0), gain=0.01
        )

        self.linear = init_(nn.Linear(num_inputs, num_outputs))

    def forward(self, x):
        x = self.linear(x)
        return FixedCategorical(logits=x)
