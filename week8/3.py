import os
path = 'D:\\pyhton\\pp2\\week8'
if os.access(path, os.F_OK):
    print(os.path.basename(path))
    print(os.path.dirname(path))