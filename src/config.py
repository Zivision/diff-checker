import os
import sys
import tomllib
import re


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


def load_conf(path: str) -> dict[str, dict[str, str]]:

    conf_path = path + "/conf.toml"
    # Check if file exists
    if not os.path.exists(conf_path):
        raise FileNotFoundError(
            f"conf.toml not found at: '{path}' file does not exist."
        )
    with open(conf_path, "rb") as f:
        return tomllib.load(f)


def parse_conf(conf: dict[str, dict[str, str]]):
    for key in conf.keys():
        if "git_project" in conf[key]:
            print(key)
            print("Bing")
        if "flake_project" in conf[key]:
            print(key)
            print("Bong")
