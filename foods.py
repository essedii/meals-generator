from classes import FoodValues as fVal


# All values have been taken from http://www.dietabit.it/, https://www.fatsecret.com/, https://www.calorieking.com/

yogurt = fVal('one cup of yogurt', 78, 6, 5, 5)
milk = fVal('one cup non-fat milk', 43, 6, 0, 4)
bread_jam = fVal('two slices whole wheat bread with two tablespoons jam', 294, 24, 3, 10)
cereals = fVal('one cup corn flakes', 91, 21, 0, 2)
salad_large = fVal('large garden salad with croutons, topped with one tablespoon oil and vinegar', 169, 37, 4, 8)
salad_small = fVal('one cup garden salad , topped with one tablespoon oil and vinegar', 92, 37, 4, 8)
broccoli = fVal('one cup steamed broccoli', 45, 9, 0, 3)
spinach = fVal('one cup cooked spinach', 12, 2, 2, 0)
chicken = fVal('chicken breast', 256, 0, 5, 52)
egg = fVal('two poached eggs (or fried in a non-stick pan)', 156, 1, 10, 12)
steak = fVal('sirloin steak', 163, 0, 5, 28)
fish = fVal('one trout filet', 380, 2, 24, 35)
pasta = fVal('one cup whole wheat pasta with one-half cup tomato sauce', 221, 46, 1, 8)
rice = fVal('one cup of rice', 332, 80, 0, 7)
avocado = fVal('one sliced avocado', 160, 8, 2, 14)
cookies = fVal('two oatmeal cookies with raisins', 130, 21, 1, 2)
apple = fVal('one apple', 48, 13, 0, 0)
banana = fVal('one banana', 89, 22, 0, 1)
orange = fVal('one orange', 7, 2, 0, 1)
beans = fVal('one cup baked beans', 238, 54, 1, 12)

first_breakfast = [yogurt, milk]
second_breakfast = [cereals, bread_jam]
fruits = [apple, banana, orange]
first_lunch = [salad_large, rice]
second_lunch = [pasta, egg]
second_snack = [avocado, cookies]
first_dinner = [chicken, steak, fish]
second_dinner = [spinach, broccoli]
third_dinner = [salad_small, beans]
