"""File to define River class."""

from ex06.fish import Fish
from ex06.bear import Bear

__author__ = "730460559"


class River:
    """River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages method."""
        fish_list: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                fish_list.append(fish)
        bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                bear_list.append(bear)
        self.fish = fish_list
        self.bears = bear_list
        return None

    def remove_fish(self, amount: int):
        """Remove fish method."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(idx)
            idx += 1
        return None

    def bears_eating(self):
        """Bears eating method."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
            else:
                bear.eat(0)
        return None

    def check_hunger(self):
        """Check hunger method."""
        bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bear_list.append(bear)
        self.bears = bear_list
        return None

    def repopulate_fish(self):
        """Repopulate fish method."""
        n: int = len(self.fish)
        while n >= 2:
            self.fish.append((n // 2) * 4)
        return None

    def repopulate_bears(self):
        """Repopulate bears method."""
        n: int = len(self.bears)
        if n >= 2:
            self.bears.append(n // 2)
        return None

    def view_river(self):
        """View river method."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week in the river."""
        count: int = 0
        while count < 7:
            self.one_river_day()
            count += 1
        return None
