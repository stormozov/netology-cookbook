# Импортирую модулю OS для работы с операционной системой
import os
# Импортирую модулю Pprint для лучшего вывода объемной информации в консоль для проверки
import pprint

# Получаю абсолютный путь к файлу с рецептами
recipes_file_path = os.path.join(os.getcwd(), 'source_files', 'recipes.txt')
# Создаю пустой словарь, в котором будут храниться данные из нужного файла
cook_book: dict = {}


def process_dish(source):
	"""
	Process the dish information from the provided file.

	Parameters:
		source (file object): The file object containing the dish information.

	Returns:
		list: A list of dictionaries, where each dictionary represents an ingredient of the dish.
		Each dictionary contains the keys 'ingredient_name', 'quantity', and 'measure'.
	"""
	dish_ingredients: list[dict] = []
	num_ingredients: int = int(source.readline())

	for _ in range(num_ingredients):
		line: str = source.readline().strip()
		if not line:
			raise ValueError("Empty line encountered")
		ingredient_name, quantity, measure = line.split(' | ')
		dish_ingredients.append({
			'ingredient_name': ingredient_name,
			'quantity': int(quantity),
			'measure': measure
		})

	return dish_ingredients


with open(recipes_file_path, encoding='UTF-8') as file:
	for line in file:
		dish_name: str = line.strip()
		while dish_name:
			cook_book[dish_name] = process_dish(file)
			dish_name = file.readline().strip()

pprint.pprint(cook_book)
