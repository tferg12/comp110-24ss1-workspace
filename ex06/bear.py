"""File to define Bear class."""


class Bear:
    """Bear Class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Simulates one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Eat method."""
        self.hunger_score += num_fish
        return None
