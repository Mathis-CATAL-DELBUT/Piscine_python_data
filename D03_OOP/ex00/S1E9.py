from abc import ABC, abstractmethod


class Character(ABC):
    """Class docstring (Character)"""

    def __init__(self, first_name, is_alive=True):
        """Method docstring (Character)"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Class docstring (Stark)"""

    def die(self):
        """Kill the character"""
        self.is_alive = False
