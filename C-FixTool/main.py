import syntax_checker
import argparse


def main(file):
	# The core of applicatoin

	# Checking that the file exists
	file_status = syntax_checker.check_file(file)
	if file_status == 0:
		print("Invalid file. Please provide a valid C file.")
		return 

	# First compilation of the C program
	if syntax_checker.compilation(file):
		print('You are lucky; your program has no errors.')
		return


	print("end of main")






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check C program syntax.")
    parser.add_argument("file", help="Path to the C file to check.")
    args = parser.parse_args()
    main(args.file)