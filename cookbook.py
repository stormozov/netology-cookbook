import get_files_paths as gfp
# I import the Pprint module to better output bulk information to the console for verification
# https://docs.python.org/3/library/pprint.html
import pprint

# I get the absolute path to the recipe file
recipes_file_path: str = gfp.get_files_by_extension('source_files', '.txt', 'recipes.txt')[
	'recipes.txt']


def process_ing_dish(file):
	"""
	Process the ingredients of the dish from the provided file.

	Parameters:
		- file (file object): The file object containing the dish information.

	Returns:
		- A list of dictionaries, where each dictionary represents an ingredient of the dish.
		Each dictionary contains the keys 'ingredient_name', 'quantity', and 'measure'.
	"""
	if file is None:
		raise ValueError("File object cannot be None")

	dish_ingredients = []
	try:
		num_ingredients = int(file.readline())
		if num_ingredients <= 0:
			raise ValueError("Number of ingredients must be a positive integer")

		for _ in range(num_ingredients):
			line = file.readline().strip()

			if not line:
				raise ValueError("Empty line encountered while processing dish ingredients")

			ingredient_name, quantity, measure = line.split(' | ')

			if len(ingredient_name.strip()) == 0 or len(quantity.strip()) == 0 or len(measure.strip()) == 0:
				raise ValueError("Invalid line encountered while processing dish ingredients")

			dish_ingredients.append({
				'ingredient_name': ingredient_name,
				'quantity': int(quantity),
				'measure': measure
			})
	except ValueError as e:
		print(f"Error: {e}")
		return []

	return dish_ingredients


def process_recipes(source_file: str, coding_standard: str) -> dict[str, list[dict]]:
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
	supported_encodings = ['utf-8', 'utf-16', 'ascii']
	cook_book: dict[str, list[dict]] = {}

	if source_file is None:
		raise ValueError("File path cannot be None")

	if coding_standard not in supported_encodings:
		raise ValueError("Unsupported encoding. Please use one of the supported encodings: utf-8, "
						 "utf-16, ascii")

	try:
		with open(source_file, encoding=coding_standard) as file:
			for line in file:
				dish_name: str = line.strip()
				cook_book[dish_name] = process_ing_dish(file)
				dish_name: str = file.readline().strip()
			return cook_book
	except IOError as e:
		print(f"Error reading file: {e}")
		return {}


cookbook: dict[str, list[dict]] = process_recipes(recipes_file_path, 'utf-8')


def generate_shopping_list(sources: dict[str, list[dict]], dishes: list[str], people: int) -> dict[
	str, dict[str, int]]:
	"""
	Generate a shopping list based on the provided dishes, number of people, and ingredients.

	Parameters:
		sources (dict): A dictionary where the keys are dish names and the values are lists
		of dictionaries representing ingredients.
		dishes (list[str]): A list of dish names to include in the shopping list.
		people (int): The number of people to consider when calculating
		ingredient quantities.

	Returns:
		dict[str, dict[str, int]]: A dictionary where the keys are ingredient names and the
		values are dictionaries containing the total quantity needed (based on people count) and the
		measure of the ingredient.
	"""
	if not isinstance(sources, dict):
		raise TypeError("sources must be a dictionary")
	if not isinstance(dishes, list):
		raise TypeError("dishes must be a list")
	if not isinstance(people, int):
		raise TypeError("people must be an integer")
	if people <= 0:
		raise ValueError("people must be a positive integer")

	ready_shopping_list = {}

	for dish in dishes:
		if dish not in sources:
			print(f"Warning: Dish '{dish}' not found in sources dictionary.")
			continue

		for ingredient in sources[dish]:
			try:
				update_shopping_list(ingredient, people, ready_shopping_list)
			except Exception as e:
				print(f"Warning: Error updating shopping list for ingredient '{ingredient}': {e}")

	return ready_shopping_list


def update_shopping_list(ingredient: dict, people: int, ready_shopping_list: dict) -> None:
	"""
	Update the shopping list with the quantity of the ingredient needed for the specified number
	of people.

	Parameters:
		ingredient (dict): A dictionary representing an ingredient with keys
		'ingredient_name', 'quantity', and 'measure'.
		people (int): The number of people to consider when calculating ingredient quantities.
		ready_shopping_list (dict): The shopping list to update with the ingredient quantity.

	Returns:
		None
	"""
	if 'ingredient_name' not in ingredient or 'quantity' not in ingredient or 'measure' not in ingredient:
		raise ValueError(
			"Ingredient dictionary must have 'ingredient_name', 'quantity', and 'measure' keys")
	if not isinstance(people, int) or people <= 0:
		raise ValueError("People must be a positive integer")

	ingredient_name = ingredient['ingredient_name']
	ingredient_quantity = ingredient['quantity'] * people
	ingredient_measure = ingredient['measure']

	try:
		if ingredient_name in ready_shopping_list:
			ready_shopping_list[ingredient_name]['quantity'] += ingredient_quantity
		else:
			ready_shopping_list[ingredient_name] = {
				'quantity': ingredient_quantity,
				'measure': ingredient_measure
			}
	except Exception as e:
		print(f"Error updating shopping list for ingredient '{ingredient_name}': {e}")


shopping_list = generate_shopping_list(cookbook, ['Запеченный картофель', 'Омлет'], 2)
