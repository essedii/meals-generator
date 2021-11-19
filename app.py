from utils import *


def main():
    print()
    menu_generator()
    print()
    print_nutritional_values()


def menu_generator():
    print(f'BREAKFAST: '
          f'{meal_generator(first_breakfast)}, '
          f'{meal_generator(second_breakfast)}, '
          f'{meal_generator(fruits)}')
    print(f'SNACK: '
          f'{meal_generator(fruits)}')
    print(f'LUNCH: '
          f'{meal_generator(first_lunch)}, '
          f'{meal_generator(second_lunch)}')
    print(f'SNACK: '
          f'{meal_generator(second_snack)}')
    print(f'DINNER: '
          f'{meal_generator(first_dinner)}, '
          f'{meal_generator(second_dinner)}, '
          f'{meal_generator(third_dinner)}')


main()



