import os.path
from abc import ABC, abstractmethod
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT
from typing import List


class Agent(ABC):

    def __init__(self, num_inputs, num_outputs):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.model_dir = None

    """
    - Abstract agent class
    """

    @abstractmethod
    def update(self, inputs, reward_collision=False, wall_collision=False, keys_pressed=None) -> List[int]:
        """
        - Given input from the simulation make a decision
        :param wall_collision: whether the car collided with the wall
        :param reward_collision: whether the car collided with a reward
        :param inputs: sensor input as a numpy array
        :param keys_pressed: a map of pressed keys
        :return direction: int [0 - num_outputs)
        """
        pass

    @abstractmethod
    def save_model(self):
        """
        - Save the brain of the agent to some file (or don't)
        :param path: the path to the model
        :return: None
        """
        pass

    @abstractmethod
    def load_model(self, path):
        """
        - Load the brain of the agent from some file (or don't)
        :param path: the path to the model
        :return: None
        """
        pass

    def set_model_dir(self, dir, force_create=False):
        """
        :param force_create:
        :param dir:
        :return:
        """
        self.model_dir = dir
        if force_create and not os.path.exists(dir):
            os.mkdir(dir)


class GameControlDriver(Agent, ABC):

    def __init__(self, num_inputs, num_outputs):
        """
        Default controls for human driver
        :param num_inputs: the number of inputs (sensors/collision/reward)
        :param num_outputs: the number of outputs (driver-actions/left/right/etc.)
        """
        super().__init__(num_inputs, num_outputs)

    def update(self, inputs, reward_collision=False, wall_collision=False, keys_pressed=None) -> List[int]:
        """
        - Encode the inputs to integers 0 - 3
        :param wall_collision: n/a
        :param reward_collision: n/a
        :param inputs: the input from the car sensors (n/a)
        :param keys_pressed: the keys pressed from the user
        :return: a list of output encodings (0 - 3) representing requested movement
        """
        ret = []
        if keys_pressed[K_LEFT]:
            ret.append(0)
        if keys_pressed[K_UP]:
            ret.append(1)
        if keys_pressed[K_RIGHT]:
            ret.append(2)
        if keys_pressed[K_DOWN]:
            ret.append(3)
        return ret

    def save_model(self):
        """
        do nothing
        :param path: n/a
        :return: n/a
        """
        pass

    def load_model(self, path):
        """
        do nothing
        :param path: n/a
        :return: n/a
        """
        pass
