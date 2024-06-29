import os
import os.path
import shutil

ROOT_DIR = os.environ['ROOT_DIR']
SAVE_DIR = os.environ['SAVE_DIR']

for f in os.listdir(ROOT_DIR):
    # Seinfeldsxdx
    if f.startswith("Seinfeld"):
        season = f[9]
        target_dir = os.path.join(SAVE_DIR, f"Season 0{season}")
        source_dir = os.path.join(ROOT_DIR, f)
        # os.makedirs(target_dir)
        for ep in os.listdir(source_dir):
            if ep.endswith('.mp4'):
                l = len(os.listdir(target_dir))
                if l < 10:
                    l = f"0{l}"
                source_file = os.path.join(source_dir, ep)
                target_file = os.path.join(target_dir, f"s0{season}e{l}.mp4")
                print(f"Move ${source_file} to ${target_file}")

    # subdir = os.path.join(ROOT_DIR, f)
    # if os.path.isdir(subdir):        
    #     f1 = os.listdir(subdir)
    #     if len(f1) == 1 and f1[0].endswith('.mkv'):
    #         old_path = os.path.join(subdir, f1[0])
    #         new_path = os.path.join(ROOT_DIR, f"{f}.mkv")
    #         print(f1[0])
    #         os.rename(old_path, new_path)
    #     else:
    #         print(f"Directory {subdir} has unexpected number of files")