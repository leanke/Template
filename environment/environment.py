import gym
from gym import spaces
import numpy as np

class Environment(gym.Env):

    def __init__(self, env_config):
        # Define action and observation space
        # They must be gym.spaces objects
        # Example: action space with 2 discrete actions
        self.action_space = spaces.Discrete(2)
        # Example: observation space with 4 continuous features
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        # Environment Config
        self.max_steps = env_config['max_steps']

    def reset(self):
        """Reset the state of the environment to an initial state"""
        self.state = np.random.rand(4) # Placeholder for observation
        self.steps = 0
        return self.state, {}

    def step(self, action):
        """Execute one time step within the environment"""
        # Placeholder for state transition logic
        self.state = np.random.rand(4) # Placeholder for observation
        reward = 1.0  # Placeholder for reward calculation
        done = False  # Placeholder for termination condition
        info = {}  # Placeholder for additional info
        if self.steps >= self.max_steps:
            info = {'reward': reward}
            done = True
        return self.state, reward, done, done, info

    def render(self, mode='human'):
        """Render the environment to the screen"""
        print(f"State: {self.state}")

    def close(self):
        """Perform any necessary cleanup"""
        pass
