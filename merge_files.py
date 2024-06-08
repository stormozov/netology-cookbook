import os
import pprint

UNICODE = 'UTF-8'


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


all_txt_file_paths: dict = get_files_by_extension('.txt')


def merge_files(source_files: list, result_file: str):
	temp_list = []
	for source_file in source_files:
		with open(source_file, 'r', encoding=UNICODE) as f:
			file_name = os.path.basename(source_file)
			file_content = f.readlines()
			temp_list.append({
				file_name: {
					'file_name': file_name,
					'count_lines': len(file_content or 0),
					'content': file_content
				}
			})

	temp_list.sort(key=lambda x: x[list(x.keys())[0]]['count_lines'])

	with open(result_file, 'w', encoding=UNICODE) as result:
		for dictionary in temp_list:
			for info in dictionary:
				result.write(f'{info}\n{dictionary[info]["count_lines"]}\n')
				for i3 in dictionary[info]['content']:
					result.write(f'{i3}')


merge_files(
	[all_txt_file_paths['1.txt'], all_txt_file_paths['2.txt'], all_txt_file_paths['3.txt']],
	all_txt_file_paths['merged_files.txt']
)
