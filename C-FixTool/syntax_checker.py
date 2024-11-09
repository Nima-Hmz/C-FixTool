import subprocess
import os

def check_file(c_file_path):
	# Check if the file exists and has .c extension
	if not os.path.isfile(c_file_path) or not c_file_path.endswith('.c'):
		return 0
	return 1

def compilation(c_file_path):
	# Check the syntax of c file (by compiling it)
    try:
        result = subprocess.run(
            ['gcc', '-fsyntax-only', c_file_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return 1
        else:
        	return 0, result.stderr
    except FileNotFoundError:
        print("GCC is not installed. Please install GCC to use this script.")
