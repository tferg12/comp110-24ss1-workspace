"""File to define Fish class."""


class Fish:
    """Fish Class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor."""
        self.age: int = 0
        return None

    def one_day(self):
        """Simulates one day."""
        self.age += 1
        return None
