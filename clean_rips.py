import os
import os.path
import shutil

ROOT_DIR = os.environ['ROOT_DIR']

for f in os.listdir(ROOT_DIR):
    subdir = os.path.join(ROOT_DIR, f)
    if os.path.isdir(subdir):        
        f1 = os.listdir(subdir)
        if len(f1) == 1 and f1[0].endswith('.mkv'):
            old_path = os.path.join(subdir, f1[0])
            new_path = os.path.join(ROOT_DIR, f"{f}.mkv")
            print(f1[0])
            os.rename(old_path, new_path)
        else:
            print(f"Directory {subdir} has unexpected number of files")