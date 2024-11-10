import os
import importlib.util

def load_modules_from_directory(directory_path):
    """Dynamically load all Python modules in a specified directory."""
    modules = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.py'):
            module_name = filename[:-3]  # Remove the '.py' extension
            file_path = os.path.join(directory_path, filename)
            
            # Load the module dynamically
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Add the module to the list of modules
            modules.append(module)
    
    return modules

def corrector(c_file_path, output_path_file, modules):
	"""Process each line of the input file using all modules and write to the output file."""
	with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
		for line in input_file:
			processed_line = line
	        # Apply each module's process_line function to the line
			for module in modules:
				processed_line = module.process_line(processed_line)
			# Write the processed line to the output file
			output_file.write(processed_line)













