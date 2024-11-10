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



modules = load_modules_from_directory('analysis/')







def corrector(c_file_path):
	pass 