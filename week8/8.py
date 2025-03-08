import os
path = 'demo.txt'
if os.access(path, os.F_OK):
    print('Path exists.')
else:
    print('Path do not exist.')
if os.access(path, os.X_OK):
    print('Path is accessible.')
else:
    print('Path is no accessible.')
if os.path.exists(path):
    os.remove(path)
