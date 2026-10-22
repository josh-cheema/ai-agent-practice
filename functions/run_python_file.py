import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_file = os.path.commonpath([absolute_path, full_path]) == absolute_path

        if not valid_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", full_path]
        if args:
            command.extend(args)

        result = subprocess.run(command, cwd=absolute_path, capture_output=True, text=True, timeout=30)
        output = ""
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}\n'
        if not result.stdout and not result.stderr:
            output += "No output produced\n"
        else:
            output += f'STDOUT: {result.stdout}\n'
            output += f'STDERR: {result.stderr}\n'
        return output
    except Exception as e:
        return f'Error: executing Python file: {str(e)}'

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs or executes a Python file in the specified working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the Python file to run or execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Arguments to pass to the Python file",
                }
            },
            "required": ["file_path"]
        }
    }
}