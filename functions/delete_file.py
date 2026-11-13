import os


def delete_file(working_directory: str, file_path: str) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_filepath = os.path.commonpath([absolute_path, full_path]) == absolute_path

        if not valid_filepath:
            return f'Error: Cannot delete "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(full_path):
            return f'Error: Cannot delete "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        os.remove(full_path)
        return f'Successfully deleted "{file_path}"'
    except Exception as e:
        return f"Error: {str(e)}"


schema_delete_file = {
    "type": "function",
    "function": {
        "name": "delete_file",
        "description": "Deletes a file in the specified working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to delete, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}
