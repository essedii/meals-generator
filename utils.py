from foods import *
from classes import PlanValues
import random


def meal_generator(meals):
    food_selected = random.choice(meals)
    update_nutrition_values(meals, food_selected)
    return food_selected


def update_nutrition_values(meals, food_selected):
    for food in meals:
        if food == food_selected:
            meals.remove(food)
            total_nutrition_values.calories += food.calories
            total_nutrition_values.carbs += food.carbs
            total_nutrition_values.fats += food.fats
            total_nutrition_values.proteins += food.proteins


def print_nutritional_values():
    print(f'CALORIES: {total_nutrition_values.calories} cal')
    print(f'CARBOHYDRATES: {total_nutrition_values.carbs} g')
    print(f'FATS: {total_nutrition_values.fats} g')
    print(f'PROTEINS: {total_nutrition_values.proteins} g')


total_nutrition_values = PlanValues(0, 0, 0, 0)
