import os

path = __file__
path = os.path.splitext(os.path.basename(path))[0]
print(path)