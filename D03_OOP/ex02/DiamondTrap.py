from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class docstring (King)"""

    def set_eyes(self, eyes):
        """Set the eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the hairs color"""
        self.hairs = hairs

    def get_eyes(self):
        """Get the eyes color"""
        return self.eyes

    def get_hairs(self):
        """Get the hairs color"""
        return self.hairs