# working with OS independent file paths

import os

def run_os_path_examples():
    """
    Examples of computing/manipulating paths reliably using the os module
    """

    # Get absolute path using os.path - note path uses backslashes on Windows
    current_abs_path = os.path.abspath("current_file.txt")
    print(current_abs_path)

    # Get absolute path to child_file.text using os.path
    child_abs_path = os.path.abspath("child/child_file.txt")
    print(child_abs_path)

    # Get current working directory
    working_dir = os.getcwd()
    print(working_dir)

    # Construct paths using os.path.join
    child_rel_path = os.path.join(working_dir, "child", "child_file.txt")
    print(child_rel_path)

    parent_rel_path = os.path.join(working_dir, os.pardir, "parent_file.txt")
    print(parent_rel_path)
