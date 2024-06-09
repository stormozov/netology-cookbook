import get_files_paths as gfp
# I import the Pprint module to better output bulk information to the console for verification
# https://docs.python.org/3/library/pprint.html
import pprint

# I get the absolute path to the recipe file
recipes_file_path: str = gfp.get_files_by_extension('source_files', '.txt', 'recipes.txt')[
	'recipes.txt']

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


cookbook: dict[str, list[dict]] = process_recipes(recipes_file_path, 'UTF-8')


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
	ready_shopping_list = {}

	for dish in dishes:
		for ingredient in sources[dish]:
			update_shopping_list(ingredient, people, ready_shopping_list)

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
	ingredient_name = ingredient['ingredient_name']
	ingredient_quantity = ingredient['quantity'] * people
	ingredient_measure = ingredient['measure']

	if ingredient_name in ready_shopping_list:
		ready_shopping_list[ingredient_name]['quantity'] += ingredient_quantity
	else:
		ready_shopping_list[ingredient_name] = {
			'quantity': ingredient_quantity,
			'measure': ingredient_measure
		}


shopping_list = generate_shopping_list(cookbook, ['Запеченный картофель', 'Омлет'], 2)
