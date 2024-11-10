import file_checker, error_corrector
import argparse


def main(file):
	"""
    The main execution function for the program.

    This function serves as the entry point for the application.
    When the user runs main.py, this function is called to start 
    the program and coordinate the core operations.
    """ 

	# Checking that the file exists
	file_status = file_checker.check_file(file)
	if file_status == 0:
		print("Invalid file. Please provide a valid C file.")
		return 

	# First compilation of the C program
	compilation_result = file_checker.compilation_test(file)
	if compilation_result[0] == 1:
		print("You're lucky; there are no errors in your program already. \n"
			"this is the output of your code:\n")
		print(file_checker.compilation('output/ready_to_run/program.out'))
		print("\nAlso you can check the output file in the output/ready_to_run directory")	
		return

	# Start analysis
	modules = error_corrector.load_modules_from_directory('analysis/')
	error_corrector.corrector(file, 'output/checked/beta/program.c', modules)

	# Checking the output of analysis
	compilation_result = file_checker.compilation_test('output/checked/beta/program.c')
	if compilation_result[0] == 1:
		print("Your program has been fixed, and you can now use it. \n"
			"this is the output of your code:\n")
		print(file_checker.compilation('output/ready_to_run/program.out'))
		print("\nAlso you can check the output file in the output/ready_to_run directory")	
		return
	else:
		print("We worked on your program file, but it was not fixed after our analysis.\n"
				"This is the error I received:\n\n"
				f"{compilation_result[1]}"
				"\nYou can view our changes to your file in the following directory:"
				"output/checked/beta/"
			)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check C program syntax.")
    parser.add_argument("file", help="Path to the C file to check.")
    args = parser.parse_args()
    main(args.file)