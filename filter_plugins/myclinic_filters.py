import pathlib
import copy

def glob_match(p, glob):
    return pathlib.PurePath(p).match(glob)

def filter_by_glob(a, glb):
    return sorted(list(filter(lambda x: glob_match(x, glb), a)))

def append_list(a, b):
    c = copy.copy(a)
    c.extend(b)
    return c

def sort_list(a):
    return sorted(a)

def replace_char(a, src, dst):
    return a.replace(src, dst)

class FilterModule(object):
    def filters(self):
        return {'filter_by_glob': filter_by_glob,
            'append_list': append_list,
            'sort_list': sort_list,
            'replace_char': replace_char}

