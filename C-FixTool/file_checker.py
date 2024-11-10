import subprocess
import os

def check_file(c_file_path):
	# Check if the file exists and has .c extension
	if not os.path.isfile(c_file_path) or not c_file_path.endswith('.c'):
		return 0
	return 1

def compilation_test(c_file_path):
	# Check if the C file has no errors(by compiling it)
    try:
        result = subprocess.run(
            ['gcc', c_file_path, '-o', 'output/program.out'],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            compilation_result = (1,)
            return compilation_result
        else:
            compilation_result = (0, result.stderr)
            return compilation_result

    except FileNotFoundError:
        print("GCC is not installed. Please install GCC to use this script.")

def compilation(c_file_path):
    # run the C file
    run_result = subprocess.run(
        [c_file_path],  
        stdout=subprocess.PIPE,
    )

    return run_result.stdout.decode()