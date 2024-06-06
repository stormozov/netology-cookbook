# Importing the OS module to work with the operating system
# https://docs.python.org/3/library/os.html
import os
# I import the Pprint module to better output bulk information to the console for verification
# https://docs.python.org/3/library/pprint.html
import pprint

# I get the absolute path to the recipe file
recipes_file_path = os.path.join(os.getcwd(), 'source_files', 'recipes.txt')


def process_ing_dish(source):
	"""
	Process the ingredients of the dish from the provided file.

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
			# If the line is empty, we raise an exception
			raise ValueError("Empty line encountered")
		ingredient_name, quantity, measure = line.split(' | ')
		dish_ingredients.append({
			'ingredient_name': ingredient_name,
			'quantity': int(quantity),
			'measure': measure
		})

	return dish_ingredients


def process_recipes(source_file: str, coding_standard: str) -> dict:
	"""
	Process the recipes from the provided file.

	Parameters:
		source_file (str): The path to the file containing the recipes.
		coding_standard (str): The coding standard of the source file.
	Returns:
		dict: A dictionary where the keys are the dish names and the values are lists
		of dictionaries, where each dictionary represents an ingredient of the dish.
		Each dictionary contains the keys 'ingredient_name', 'quantity' and 'measure'.
	"""
	with open(source_file, encoding=coding_standard) as file:
		# I create an empty dictionary to store data from the required file
		cook_book: dict[str, list[dict]] = {}
		for line in file:
			# We go through each line of the recipe file and
			# call the process_dish function to process the ingredients
			dish_name: str = line.strip()
			cook_book[dish_name] = process_ing_dish(file)
			dish_name: str = file.readline().strip()
		return cook_book


pprint.pprint(process_recipes(recipes_file_path, 'UTF-8'))
