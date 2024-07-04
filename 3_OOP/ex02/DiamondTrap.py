from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class, inherits from Baratheon and Lannister"""
    def get_eyes(self):
        """Return eyes color"""
        return self.eyes

    def get_hairs(self):
        """Return hairs color"""
        return self.hairs

    def set_eyes(self, eyes):
        """Set eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set hairs color"""
        self.hairs = hairs
