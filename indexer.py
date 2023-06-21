import os
folder = "posts/"
filelist = os.listdir(folder)
subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
subfolders = [ f for f in subfolders if os.path.exists(f + "index.md")]
subfoldernames = [f[len(folder):] for f in subfolders]
indexed_list = ""

base_url = "https://ozgurseker.github.io/blog/"
folder_url = base_url + folder

filelist = [x for x in filelist if x.endswith('.md')]
full_list = [os.path.join(folder,i) for i in filelist]
time_sorted_list = sorted(full_list, key=os.path.getmtime)
sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]


if "index.md" in filelist:
    if len(subfolders) > 0:
        indexed_list = indexed_list + "# Subtopics \n\n"
        
    for i in range(len(subfolders)):
        fname = subfoldernames[i]
        subfold = subfolders[i]
        folder_url = base_url + subfold
        indexed_list = indexed_list + "[" + fname + "](" + folder_url + ") \n \n"
    
    if len(filelist) > 1:
        indexed_list = indexed_list + "# Posts \n\n"
        
        
    for name in sorted_filename_list:
        if name == "index.md":
            None
        else:
            page_url = folder_url + name[:-3]
            indexed_list = indexed_list + "[" + name[:-3] + "](" + page_url + ") \n \n"
            
    with open(folder + "index.md", 'w') as f:
        f.write(indexed_list)