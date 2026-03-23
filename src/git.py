import os


def git_run(git_data: dict[str, str]) -> None:
    current_local_commit = git_current_local_commit(
        git_data["git_local_path"], git_data["git_branch"]
    )
    print(current_local_commit)


def git_current_local_commit(path: str, branch: str) -> str:
    with open((os.path.expanduser(path) + "/.git/refs/heads/" + branch), "r") as f:
        return f.read()
