class PlanValues:
    def __init__(self, calories, carbs, fats, proteins):
        self.calories = calories
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins


class FoodValues:
    def __init__(self, name, calories, carbs, fats, proteins):
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins

    def __str__(self):
        return self.name


