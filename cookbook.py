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


# pprint.pprint(process_recipes(recipes_file_path, 'UTF-8'))

cookbook: dict[str, list[dict]] = process_recipes(recipes_file_path, 'UTF-8')


def get_shop_list_by_dishes(source: dict, dishes: list[str], person_count: int) -> dict[str, dict[str, int]]:
	"""
	Generate a shopping list based on the provided dishes, number of people, and ingredients.

	Parameters:
		source (dict): A dictionary where the keys are dish names and the values are lists
		of dictionaries representing ingredients.
		dishes (list[str]): A list of dish names to include in the shopping list.
		person_count (int): The number of people to consider when calculating
		ingredient quantities.

	Returns:
		dict[str, dict[str, int]]: A dictionary where the keys are ingredient names and the
		values are dictionaries containing the total quantity needed (based on person count) and the
		measure of the ingredient.
	"""
	generated_shop_list: dict = {}

	for dish in dishes:
		for ingredient in source[dish]:
			# Multiply the quantity of the ingredient by the number of people
			ingredient_name = ingredient['ingredient_name']
			# Create a dictionary with the quantity and measure
			ingredient_dict = {
				'quantity': ingredient['quantity'] * person_count,
				'measure': ingredient['measure']
			}

			# Check if the ingredient is already in the generated shop list
			if ingredient_name in generated_shop_list:
				# If the ingredient is already in the generated shop list, we add the quantity
				generated_shop_list[ingredient_name]['quantity'] += ingredient_dict['quantity']
			else:
				# If the ingredient is not in the generated shop list, we add it
				generated_shop_list[ingredient_name] = {
					'quantity': ingredient_dict['quantity'],
					'measure': ingredient_dict['measure']
				}

	return generated_shop_list


shop_list = get_shop_list_by_dishes(cookbook, ['Запеченный картофель', 'Омлет'], 2)
pprint.pprint(shop_list)
