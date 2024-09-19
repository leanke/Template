# from pufferlib.models import Default as Policy
from pdb import set_trace as T
from functools import partial
import torch

import pufferlib.models


class Recurrent(pufferlib.models.LSTMWrapper):
    def __init__(self, env, policy,
            input_size=512, hidden_size=512, num_layers=1):
        super().__init__(env, policy,
            input_size, hidden_size, num_layers)

class Policy(pufferlib.models.Default):
    def __init__(self, env, hidden_size=128):
        super().__init__(
            env=env,
            hidden_size=hidden_size,
        )