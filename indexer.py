import os
folder = "posts/"
filelist = os.listdir(folder)
if "index.md" in filelist:
    for name in [x for x in filelist if x.endswith('.md')]:
        if name == "index.md":
            
        else:
            