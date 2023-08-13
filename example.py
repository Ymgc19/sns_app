import os

path = __file__
path = str(os.path.splitext(os.path.basename(path))[0])

ext = ".csv"

path = path + ext
print(path)