from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True):
        """Initialize Baratheon"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):
        return f"Vector: {tuple([self.family_name, self.eyes, self.hairs])}"

    def __str__(self):
        return f"Vector: {tuple([self.family_name, self.eyes, self.hairs])}"


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name, is_alive=True):
        """Initialize Lannister"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        return f"Vector: {tuple([self.family_name, self.eyes, self.hairs])}"

    def __str__(self):
        return f"Vector: {tuple([self.family_name, self.eyes, self.hairs])}"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister"""
        return (cls(first_name, is_alive))
