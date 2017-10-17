import os
import sys

ALLOWED_EXTENSIONS = ['c', 'py', 'pl']

EXTENSIONS = {
    'c': ['c', 'h'],
    'py': ['py', 'pyc'],
    'pl': ['pl', 'pm']}


def get_extensions(extensions):
    result = []
    for extension in extensions:
        result.extend(EXTENSIONS[extension])
    return result


def validate_extensions(*args):
    for arg in args:
        if arg not in ALLOWED_EXTENSIONS:
            raise AttributeError('Not supported extension %s' % arg)


def walk(directory, extensions):
    extensions = get_extensions(extensions)
    file_list = os.listdir(directory)
    result = []
    for elem in file_list:
        full_path = os.path.join(directory, elem)
        if not os.path.isfile(full_path):
            continue
        for extension in extensions:
            if full_path.endswith(extension):
                result.append(elem)
    return result

if __name__ == '__main__':
    args = sys.argv[1:]
    validate_extensions(*args)
    cwd = os.getcwd()
    print(walk(cwd, args))
