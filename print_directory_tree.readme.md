Walk a Directory in Python

Submitted by NanoDano on Mon, 11/12/2018 - 00:12
Overview

    Introduction
    Print a directory tree
    List file sizes in a directory recursively
    Using os.walk() to get the total size of a directory
    Recursively copy from one directory to another
    Conclusion
    Reference links

Introduction

A common task when working with files is to walk through a directory, that is, recursively get every file in every directory starting in some location. The Python 3 os module has several functions useful for working with files and directories. One in particular, os.walk() is useful for recursively going through a directory and getting the contents in a structured way. These examples will show you a couple options for walking a directory recursively.
Print a directory tree

This example will recursively walk through a directory and only print out names of directories. It will ignore files.

# print_dirs.py
import os

def print_dirs_recursively(root_dir):
    root_dir = os.path.abspath(root_dir)
    print(root_dir)

    for item in os.listdir(root_dir):
        item_full_path = os.path.join(root_dir, item)
        if os.path.isdir(item_full_path):
            print_dirs_recursively(item_full_path)

List file sizes in a directory recursively

You can walk yourself by getting the contents of a directory, seeing if it's a file or a directory, and recursing. This example will provide a function that will recurse through a directory, and print out every file with its size.

# recurse_dir.py
import os

# Print every file with its size recursing through dirs
def recurse_dir(root_dir):
    root_dir = os.path.abspath(root_dir)
    for item in os.listdir(root_dir):
        item_full_path = os.path.join(root_dir, item)

        if os.path.isdir(item_full_path):
            recurse_dir(item_full_path)
        else:
            print("%s - %s bytes" % (item_full_path, os.stat(item_full_path).st_size))

Using os.walk() to get the total size of a directory

There's nothing wrong with the examples above, but there is a more powerful way to go through directories recursively, and that is with the os.walk() function. The os.walk() function is powerful because it gives some structure to the recursion. In the previous examples, if we wanted a list of directories and a list of files in two separate lists for each directory we recurse, we'd have to make it ourselves. With os.walk we get a tuple for every directory that contains the path, a list of directories, and a list of files. You can walk a directory top down or bottom up. It defaults to top down which is usually more convenient and expected. This example will walk through a directory and sum up the total file sizes.

# dir_size.py
import os

def dir_size(root_dir):
    total_size = 0
    for (dirpath, dirs, files) in os.walk(root_dir):
        for filename in files:
            file_size = os.stat(filename).st_size
            total_size += file_size
            print("%s - %s bytes" % (os.path.join(dirpath, filename), file_size))
    print("Total size: %d" % total_size)

if __name__ == '__main__':
    # Get full size of home directory
    dir_size(os.expanduser("~"))

Recursively copy from one directory to another

The shutil module in the standard library provides a function called shutil.copytree() which will copy one directory tree to a new location. It requires the target directory to be non-existent though. It will fail if the destination directory exists. This function demonstrated below will copy to a target directory even if it exists. It will overwrite files if they already exist and create directories if needed.

# copy_recursive.py
import os
import shutil
import sys
from pathlib import Path


def copy_recursive(source_base_path, target_base_path):
    """
    Copy a directory tree from one location to another. This differs from shutil.copytree() that it does not
    require the target destination to not exist. This will copy the contents of one directory in to another
    existing directory without complaining.
    It will create directories if needed, but notify they already existed.
    If will overwrite files if they exist, but notify that they already existed.

    :param source_base_path: Directory path
    :param target_base_path: Directory path
    :return: None
    """
    if not Path(source_base_path).is_dir() or not Path(target_base_path).is_dir():
        raise Exception("Source and destination directory and not both directories.\nSource: %s\nTarget: %s" % (
        source_base_path, target_base_path))
    for item in os.listdir(source_base_path):
        # Directory
        if os.path.isdir(os.path.join(source_base_path, item)):
            # Create destination directory if needed
            new_target_dir = os.path.join(target_base_path, item)
            try:
                os.mkdir(new_target_dir)
            except OSError:
                sys.stderr.write("WARNING: Directory already exists:\t%s\n" % new_target_dir)

            # Recurse
            new_source_dir = os.path.join(source_base_path, item)
            copy_recursive(new_source_dir, new_target_dir)
        # File
        else:
            # Copy file over
            source_name = os.path.join(source_base_path, item)
            target_name = os.path.join(target_base_path, item)
            if Path(target_name).is_file():
                sys.stderr.write("WARNING: Overwriting existing file:\t%s\n" % target_name)
            shutil.copy(source_name, target_name)

Conclusion

After reading this, you should be able to walk through a directory recursively and get the file information you need.
Reference links

    Python 3 os module odcumentation
    os.walk()
    Python 3 shutil module documentation
    shutil.copytree()

