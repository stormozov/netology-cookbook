import os
import get_files_paths as gfp
import pprint

UNICODE = 'UTF-8'
all_txt_file_paths: dict = gfp.get_files_by_extension('source_files', '.txt')


def merge_files(source_files: list, result_file: str):
    temp_list = []
    for source_file in source_files:
        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                file_name = os.path.basename(source_file)
                file_content = f.readlines()
                temp_list.append({
                    file_name: {
                        'file_name': file_name,
                        'count_lines': len(file_content),
                        'content': file_content
                    }
                })
        except (FileNotFoundError, OSError) as e:
            print(f"An error occurred while reading {source_file}: {e}")

    temp_list.sort(key=lambda x: x[list(x.keys())[0]]['count_lines'])

    with open(result_file, 'w', encoding='utf-8') as result:
        for dictionary in temp_list:
            for info in dictionary:
                result.write(f'{info}\n{dictionary[info]["count_lines"]}\n')
                for i3 in dictionary[info]['content']:
                    result.write(f'{i3}')


merge_files(
	[all_txt_file_paths['1.txt'], all_txt_file_paths['2.txt'], all_txt_file_paths['3.txt']],
	all_txt_file_paths['merged_files.txt']
)
