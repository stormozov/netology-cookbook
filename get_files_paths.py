import os


def get_files_by_extension(directory: str, extension: str = None, filename: str = None) -> dict[str, str]:
    """
    Recursively traverses a given directory, collecting and returning a sorted dictionary of
    all files with their full path within it, filtered by extension and filename (if provided).

    Args:
        - directory: The directory path to traverse.
        - extension: The file extension to filter the files by.
        - filename: The name of the file to search for (optional).

    Returns:
        - A dictionary where keys are file names and values are their full paths found within
        the specified directory path.

    Example:
        get_files_by_extension('/path/to/directory', '.txt', 'example.txt')
    """
    if not os.path.exists(directory):
        raise NotADirectoryError(f'Directory "{directory}" does not exist')

    file_dict = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if (extension is None or file.endswith(extension)) and (filename is None or file == filename):
                file_dict[file] = os.path.abspath(os.path.join(root, file))
    return file_dict
