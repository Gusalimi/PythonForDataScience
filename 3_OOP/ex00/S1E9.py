from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Kill Character"""
        self.is_alive = False


class Stark(Character):
    """Stark class, inherits from Character"""
    def __init__(self, first_name, is_alive=True):
        """Initialize Stark"""
        super().__init__(first_name, is_alive)
