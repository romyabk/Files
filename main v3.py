__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil 
import zipfile

folder = os.getcwd()
folder_cache = os.path.join(folder, 'cache')
zip_file = folder + "/data.zip"

# Opdracht 1
def clean_cache():
    folder_check = os.listdir(folder)
    if 'cache' in folder_check:
        #delete folder
        shutil.rmtree(folder_cache)    
    #create folder
    os.mkdir(folder_cache)
    return

# Opdracht 2
def cache_zip(zip_file, folder_cache):
    with zipfile.ZipFile(zip_file, 'r',) as zip_ref:
        zip_ref.extractall(folder_cache)
    return 

# Opdracht 3
def cached_files():
    list_of_files = []
    with os.scandir(folder_cache) as list_of_entries:
        for entry in list_of_entries:
            if entry.is_file():
                result = os.path.abspath(entry)
                list_of_files.append(result)
    return list_of_files

# Opdracht 4
def find_password(fist_of_files):
  list = cached_files()
  for file in list:
    with open(file) as f:
      if 'password' in f.read():
        with open(str(file)) as p:
          for lines in p:
            if 'password' in lines:
              password = lines.strip('password: ')
              password = password.strip()
              print(password)
        return password


