import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:    
        absolute_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(absolute_path, directory))
        valid_directory = os.path.commonpath([absolute_path, full_path]) == absolute_path

        if not valid_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        result = "Result for current directory:\n"
        for item in os.listdir(full_path):
            try:
                size = os.path.getsize(os.path.join(full_path, item))
                is_dir = os.path.isdir(os.path.join(full_path, item))
            except Exception as e:
                return f'Error: {str(e)}'
            result += f'\t - {item}: file_size={size} bytes, is_dir={is_dir}\n'

        return result
    except Exception as e:
        return f'Error: {str(e)}'