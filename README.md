# files_folders
A little Python 3.4 module to get the size of a folder and get the count of the files and subfolders in it.

*FUNCTIONS*:
```python
getfilescount(start_path):
    """
    This function will return the number of the files in the given folder.
    Example: getfilescount('C:/Users/Foobar/Documents')
    :param start_path: The string (str) variable of the selected folder's path.
    :return: The number of the files in the given folder.
    """
```
```python
getfolderscount(start_path):
    """
    This function will return the number of the subfolders in the given folder.
    Example: getfolderscount('C:/Users/Foobar/Documents')
    :param start_path: The string (str) variable of the selected folder's path.
    :return: The number of the subfolders in the given folder.
    """
```
```python
getfoldersize(start_path):
    """
    This function will return the size of the given folder.
    Example: getfoldersize('C:/Users/Foobar/Documents')
    :param start_path: The string (str) variable of the selected folder's path.
    :return: Size of the folder in 'B/kB/MB/GB/TB'.
    """
```
