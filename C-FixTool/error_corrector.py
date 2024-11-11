import os
import importlib.util

def load_modules_from_directory(directory_path):
    """Dynamically load specified Python modules in a fixed order."""
    # Define the desired order of modules
    ordered_module_names = ['missing_semicolons', 'missing_parenthesesclosed', 'key_words']
    modules = []
    
    for module_name in ordered_module_names:
        filename = f"{module_name}.py"
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path):  # Check if the file exists
            # Load the module dynamically
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Add the module to the list of modules
            modules.append(module)
    
    return modules

def corrector(input_file_path, output_file_path, modules):
	"""Process each line of the input file using all modules and write to the output file."""
	with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
		for line in input_file:
			processed_line = line
	        # Apply each module's process_line function to the line
			for module in modules:
				processed_line = module.process_line(processed_line)
			# Write the processed line to the output file
			output_file.write(processed_line + '\n' if not processed_line.endswith('\n') else processed_line)