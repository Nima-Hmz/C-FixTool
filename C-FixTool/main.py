import file_checker
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
		print(file_checker.compilation('output/program.out'))
		print("\nAlso you can check the output file in the output directory")	
		return


	print("end of main")






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check C program syntax.")
    parser.add_argument("file", help="Path to the C file to check.")
    args = parser.parse_args()
    main(args.file)