#!/usr/bin/python3
import dis
import sys

def module_names(module_name):
    try:
        module = __import__(module_name[:-4])  # Import the module without the .pyc extension
    except ImportError:
        print(f"Error: Failed to import module '{module_name}'")
        sys.exit(1)

    names = [name for name in dir(module) if not name.startswith("__")]  # Get names excluding those starting with __
    sorted_names = sorted(names)  # Sort the names alphabetically

    for name in sorted_names:
        print(name)

if __name__ == "__main__":
    module_name = "hidden_4.pyc"
    module_names(module_name)
