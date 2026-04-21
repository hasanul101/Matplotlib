class Pokemon:
    def __init__(self, name, level):
        self.name = name
        # We'll use a private attribute for level
        self._level = level

    # Getter: retrieve the level
    @property
    def level(self):
        print(f"Getting level of {self.name}")
        return self._level

    # Setter: set the level with validation
    @level.setter
    def level(self, value):
        if value < 1:
            print(
                f"Level cannot be less than 1. Setting {self.name}'s level to 1.")
            self._level = 1
        elif value > 100:
            print(
                f"Level cannot exceed 100. Setting {self.name}'s level to 100.")
            self._level = 100
        else:
            print(f"Setting level of {self.name} to {value}")
            self._level = value

    # Deleter: remove the level (rarely used but possible)
    @level.deleter
    def level(self):
        print(f"Deleting level of {self.name}")
        del self._level


# Example usage
pikachu = Pokemon("Pikachu", 25)

# Access the level (getter)
print(pikachu.level)  # Getting level of Pikachu -> 25

# Update the level (setter)
pikachu.level = 50    # Setting level of Pikachu to 50
pikachu.level = 150   # Level cannot exceed 100 -> sets to 100
pikachu.level = -5    # Level cannot be less than 1 -> sets to 1

# Delete the level (deleter)
del pikachu.level
# print(pikachu.level)  # This would now raise an AttributeError
