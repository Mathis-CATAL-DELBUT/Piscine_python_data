from S1E9 import Character


class Baratheon(Character):
    """Class docstring (Baratheon)"""

    def __init__(self, first_name, is_alive=True):
        """Method docstring (Baratheon)"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill the character"""
        self.is_alive = False

    def __str__(self):
        """Write the vector as a string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Write the vector as a string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Class docstring (Lannister)"""

    def __init__(self, first_name, is_alive=True):
        """Method docstring (Lannister)"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister"""
        return cls(first_name, is_alive)

    def die(self):
        """Kill the character"""
        self.is_alive = False

    def __str__(self):
        """Write the vector as a string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Write the vector as a string"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
