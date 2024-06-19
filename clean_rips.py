import os
import os.path
import shutil

ROOT_DIR = os.environ['ROOT_DIR']

for f in os.listdir(ROOT_DIR):
    if os.path.isdir(f):
        subdir = os.path.join(ROOT_DIR, f)
        f1 = os.listdir(subdir)
        if len(f1) == 1:
            print("hit")
        else:
            print(f1)