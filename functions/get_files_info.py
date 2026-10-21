import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:    
        absolute_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(absolute_path, directory))
        valid_directory = os.path.commonpath([absolute_path, full_path]) == absolute_path

        if not valid_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'

        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f'Error: {str(e)}'