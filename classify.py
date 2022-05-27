import os
import sys


"""
This file has been created to classify easily samples in drums kits directory from the website
'https://www.thekitplug.com' that are not already classified.
To use this file, run it with python3 with as parameters the folders wherein there are files to classify 
(normally, the drums kit folders).
"""


def create_folders(path):
    """
    create missing folders to classify files
    :param (String) path: path folder of the folder wherein creating folders
    """
    folders = set()
    items = os.listdir(path)
    for item in items:
        if os.path.isfile(path + '\\' + item) and item[-4:] == '.wav':
            folders.add(item.split(' ')[0])
    for folder in folders:
        try:
            os.mkdir(path + '\\' + folder)
        except FileExistsError:
            print(''.join(["WARNING : Folder '", path + '\\' + item, "' already exists"]))


def classify(path):
    """
    classify every file in his folder
    :param path: path folder of the folder to classify
    """
    items = os.listdir(path)
    for item in items:
        if os.path.isfile(path + '\\' + item) and item[-4:] == '.wav':
            os.rename(path + '\\' + item, path + '\\' + item.split(' ')[0] + '\\' + item)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('No path given')
    for arg in sys.argv[1:]:
        create_folders(arg)
        classify(arg)
