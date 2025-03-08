import os
path = 'D:\pyhton\pp2\week8\ex.txt'
if os.access(path, os.F_OK):
    print('Path exists.')
else:
    print("Path doesn't exist")
if os.access(path, os.R_OK):
    print('Path is readable.')
else:
    print("Path is not readable.")
if os.access(path, os.W_OK):
    print('Path is writable.')
else:
    print("Path is not writable.")
if os.access(path, os.X_OK):
    print('Path is executable.')
else:
    print("Path is not executable.")