# Импортирую модулю OS для работы с операционной системой
import os
import pprint

# Получаю абсолютный путь к файлу с рецептами
recipes_file_path = os.path.join(os.getcwd(), 'source_files', 'recipes.txt')

cook_book: dict = {}

with open(recipes_file_path, encoding='UTF-8') as file:
	for line in file:
		dish_name: str = line.strip()
		while dish_name:
			dish_ingredients: list[dict] = []
			ingredients_quantity: int = int(file.readline())
			for _ in range(ingredients_quantity):
				ingredient_name, quantity, measure = file.readline().strip().split(' | ')
				dish_ingredients.append({
					'ingredient_name': ingredient_name,
					'quantity': int(quantity),
					'measure': measure
				})
			cook_book[dish_name] = dish_ingredients
			dish_name = file.readline().strip()

pprint.pprint(cook_book)
