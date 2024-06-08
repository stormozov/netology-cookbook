import os


def get_files_by_extension(file_extension: str) -> dict:
	"""
	Recursively traverses a given directory path, collecting and returning a sorted dictionary of
	all files with their full path within it.

	Args:
	- file_extension: The file extension to filter the files by.

	Returns:
		- A dictionary where keys are file names and values are their full paths found within
	the specified directory path.
	"""
	directory_path: str = os.path.join(os.path.dirname(__file__))

	if not os.path.exists(directory_path):
		raise ValueError(f'Directory "{directory_path}" does not exist')

	file_dict: dict = {}

	for root, dirs, files in os.walk(directory_path):
		for file in files:
			if file_extension is None or file.endswith(file_extension):
				file_dict[file] = os.path.join(root, file)

	return file_dict
