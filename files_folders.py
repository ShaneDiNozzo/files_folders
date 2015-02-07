__author__ = 'Shane DiNozzo'

"""##########
WIP Project!#
##########"""

import os


def getfoldersize(start_path):
    """
    This function will return the size of the given folder.
    Example: getfoldersize('C:/Users/Foobar/Documents')
    :param start_path: The string (str) variable of the selected folder's path.
    :return: Size of the folder with 'B/kB/MB/GB/TB' suffix.
    """

    total_size = 0
    total_size_twodecimal = ''

    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            total_size += os.path.getsize(filepath)

    if 1 <= len(str(total_size)) <= 3:
        total_size_twodecimal = '%.2f' % total_size + ' B'
    elif 4 <= len(str(total_size)) <= 6:
        total_size_in_kb = total_size / 1024
        total_size_twodecimal = '%.2f' % total_size_in_kb + ' kB'
    elif 7 <= len(str(total_size)) <= 9:
        mb = 1024 * 1024
        total_size_in_mb = total_size / mb
        total_size_twodecimal = '%.2f' % total_size_in_mb + ' MB'
    elif 10 <= len(str(total_size)) <= 12:
        gb = 1024 * 1024 * 1024
        total_size_in_gb = total_size / gb
        total_size_twodecimal = '%.2f' % total_size_in_gb + ' GB'
    elif 13 <= len(str(total_size)) <= 15:
        tb = 1024 * 1024 * 1024 * 1024
        total_size_in_tb = total_size / tb
        total_size_twodecimal = '%.2f' % total_size_in_tb + ' TB'
    else:
        print('The size of the folder is greater than TB!')

    return total_size_twodecimal


def getfilescount(start_path):
    """
    This function will return the number of the files in the given folder.
    Example: getfilescount('C:/Users/Foobar/Documents')
    :param start_path: The string (str) variable of the selected folder's path.
    :return: The number of the files in the given folder with 'file(s)' suffix.
    """

    count = 0
    for f in os.listdir(start_path):
        if os.path.isfile(os.path.join(start_path, f)):
            count += 1

    return str(count) + ' file(s)'


def getfolderscount(start_path):
    """
    This function will return the number of the subfolders in the given folder.
    Example: getfolderscount('C:/Users/Foobar/Documents')
    :param start_path: The string (str) variable of the selected folder's path.
    :return: The number of the subfolders in the given folder with 'folder(s)' suffix.
    """

    foldercount_array = [os.path.join(start_path, o) for o in os.listdir(start_path) if
                         os.path.isdir(os.path.join(start_path, o))]

    return str(foldercount_array.__len__()) + ' folder(s)'
