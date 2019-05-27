import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix is not None and path is not None:
        pathList = []
        for root, dirs, files in os.walk("./" + path):
            for file in files:
                if file.endswith("." + suffix):
                    pathList.append(root)
        return pathList
    else:
        return 'Not Valid'
 
'''
TEST
'''
def test1(charVal, folder):
    listValues = find_files(charVal, folder)
    return listValues == ['./testdir', './testdir/subdir3/subsubdir1', './testdir/subdir5', './testdir/subdir1']
print(test1('c', 'testdir'))
# True

def test2(charVal, folder):
    listValues = find_files(charVal, folder)
    return listValues == ['./testdir', './testdir/subdir3/subsubdir1', './testdir/subdir5', './testdir/subdir1']
print(test2('c', None))
# False

def test3(charVal, folder):
    listValues = find_files(charVal, folder)
    return listValues == ['./testdir', './testdir/subdir3/subsubdir1', './testdir/subdir5', './testdir/subdir1']
print(test3('', ''))
# False