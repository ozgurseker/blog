import os
folder = "posts/"
filelist = os.listdir(folder)
indexed_list = ""
base_url = "https://ozgurseker.github.io/blog/"
folder_url = base_url + folder
if "index.md" in filelist:
    for name in [x for x in filelist if x.endswith('.md')]:
        if name == "index.md":
            None
        else:
            page_url = folder_url + name[:-3]
            indexed_list = indexed_list + "[" + name[:-3] + "](" + page_url + ") \n \n"
            
    with open(folder + "index.md", 'w') as f:
        f.write(indexed_list)