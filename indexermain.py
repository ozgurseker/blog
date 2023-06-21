import os
import glob
folder = ""
filelist = os.listdir()
subfolders = [ f.path for f in os.scandir() if f.is_dir() ]
subfolders = [ f for f in subfolders if os.path.exists(f + "/index.md")]
subfoldernames = [f[len(folder):] for f in subfolders]
indexed_list = ""

base_url = "https://ozgurseker.github.io/blog/"
folder_url = base_url + folder

lst_files = glob.glob("**/*.md", recursive= True)
lst_files.sort(key=os.path.getmtime)
lst_files = [i for i in lst_files if not i == "README.md"]
lst_files = [i for i in lst_files if not i == "about.md"]

sorted_filename_list = [ os.path.basename(i) for i in lst_files if os.path.basename(i) != "index.md"]
lst_files = [ i for i in lst_files if os.path.basename(i) != "index.md"]

if len(subfolders) > 0:
    indexed_list = indexed_list + "# Subtopics \n\n"
    
for i in range(len(subfolders)):
    fname = subfoldernames[i]
    subfold = subfolders[i]
    folder_url = base_url + subfold
    indexed_list = indexed_list + "[" + fname + "](" + folder_url + ") \n \n"

if len(sorted_filename_list) > 0:
    indexed_list = indexed_list + "# All Posts \n\n"
    
    
for i in range(len(sorted_filename_list)):
    name = sorted_filename_list[i]
    file = lst_files[i]
    if name == "index.md":
        None
    else:
        page_url = base_url + file[:-3]
        indexed_list = indexed_list + "[" + name[:-3] + "](" + page_url + ") \n \n"
        
with open(folder + "index.md", 'w') as f:
    f.write(indexed_list)