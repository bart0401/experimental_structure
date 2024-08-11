# -*- coding: utf-8 -*-

# Library & module
import os

def directory_tree(path):
    for path, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ['.idea', '__pycache__']]
        depth = len(path.split(os.sep)) - 1
        indent = ' ' * 4 * (depth)
        if os.path.basename(path):
            print('{}+{}/'.format(indent, os.path.basename(path)))
        subindent = ' ' * 4 * (depth + 1)
        for f in files:
            # Exclude .jpg files
            if not f.endswith(('.jpg', '.pkl', '.pth')):
                print('{}|-{}'.format(subindent, f))

directory_tree(os.getcwd())
#%%