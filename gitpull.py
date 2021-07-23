"""Pull each project's repository in current directory."""

import os
import subprocess

from termcolor import cprint

root = os.getcwd()
projects: list = [project for project in os.listdir() if os.path.isdir(project)]
print(projects)
for project in projects:
    filename = os.path.basename(project)
    if "wp" in filename:
        continue
    try:
        cprint(f"\n\nChecking {filename}......", "cyan", attrs=["bold"])
        subprocess.run(["git", "-C", f"{root}/{project}", "pull"], check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(project) from e
