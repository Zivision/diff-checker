import os
import sys


# Default path for config file
def set_path(path: str = "~/.config/diff-checker") -> str | None:
    # First check if path exists
    true_path = os.path.expanduser(path)
    if os.path.exists(true_path):
        return true_path

    # Ask for user input if path doesn't exist
    while True:
        prompt = input(f"Path: '{path}' doesn't exists! Create it? (y or n): ")
        if prompt == "y" or prompt == "yes":
            os.makedirs(true_path, exist_ok=True)
            return true_path
        elif prompt == "n" or prompt == "no":
            print("Nothing was made! Exiting program")
            sys.exit(0)
        else:
            print("Invalid input!")
