import os
import sys


"""
This file has been created to rename easily samples in drums kits directory from the website
'https://www.thekitplug.com'.
To use this file, run it with python3 with as parameters the folders wherein there are files to rename 
(normally, the drums kit folders).
"""


def rename_file(file_path):
    """
    rename the file name
    from '<compilation_name> - <instrument> - <id>.wav'
    into '<id> - <instrument> - <compilation_name>.wav'
    :param (String) file_path: file path of the file to rename
    """
    split_path = file_path.split('\\')
    words = split_path[-1].split(' ')
    file_name = ' '.join(words[2:])[:-4]
    file_name = ' '.join([file_name, words[1], words[0], '.wav'])
    os.rename(file_path, '\\'.join(split_path[:-1] + [file_name]))


def rename_files(path):
    """
    recursively rename every file .wav in a given folder thanks to the rename_file function
    :param (String) path: path of the file to rename or the folder wherein are located the files to rename
    """
    if os.path.isfile(path) and path[-4:] == '.wav':
        rename_file(path)
    elif os.path.isdir(path):
        items = os.listdir(path)
        for item in items:
            rename_files(path+'\\'+item)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('No path given')
    for arg in sys.argv[1:]:
        rename_files(arg)
