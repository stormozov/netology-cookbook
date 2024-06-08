import os
import pprint

UNICODE = 'UTF-8'


def generate_file_path(file_name, folder_name='source_files'):
	return os.path.join(os.getcwd(), folder_name, file_name)


file_1 = generate_file_path('1.txt', 'source_files/sorted')
file_2 = generate_file_path('2.txt', 'source_files/sorted')
file_3 = generate_file_path('3.txt', 'source_files/sorted')
result_file = generate_file_path('merged_files.txt')


def count_number_rows(source):
	count: int = 0
	for _ in source:
		count += 1
	return count


def merge_files(source_file_1, source_file_2, source_file_3, result_file):
	with (open(source_file_1, 'r', encoding=UNICODE) as f1,
		  open(source_file_2, 'r', encoding=UNICODE) as f2,
		  open(source_file_3, 'r', encoding=UNICODE) as f3):
		temp_list = []
		file_content = f1.readlines()
		file_lines_count = count_number_rows(file_content)
		file_name = os.path.basename(source_file_1)
		temp_list.append({
			file_name: {
				'file_name': file_name,
				'count_lines': file_lines_count,
				'content': file_content
			}
		})

		with open(result_file, 'w', encoding=UNICODE) as result:
			for dictionary in temp_list:
				for info in dictionary:
					result.write(f'{info}\n{dictionary[info]["count_lines"]}\n')
					for i3 in dictionary[info]['content']:
						result.write(f'{i3}')


merge_files(file_1, file_2, file_3, result_file)
