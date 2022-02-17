import shutil
import os
import glob
import time

# Here we define  where search the files to order.
PATH_FILES = "c:/Users/B14573R/Desktop/"

# Here we define  that extension moved to the folders created.
SEARCH_FILES = "c:/Users/B14573R/Desktop/*."

# Here we define the paths source and destination for moved files.
PATH_SRC = "c:/Users/B14573R/Desktop/Archivos "


list_files = os.listdir(PATH_FILES)
extension_list = []
for file in range(0,len(list_files)):
    extension = (os.path.splitext(list_files[file])[1]).replace(".","")
    if not extension in extension_list and extension != "":
        extension_list.append(extension)#[exe,pdf,html...]

for file_type in extension_list:
    search_extension = glob.glob(SEARCH_FILES + file_type)
    directory_exists = os.path.exists(PATH_SRC + file_type)
    print(search_extension)
    for select_extension in search_extension:
        if  directory_exists:
            print("Moving the file to: ",shutil.move(str(select_extension),PATH_SRC + file_type))
            time.sleep(1)
        else:
            os.mkdir(PATH_SRC + file_type)
            print("Moving the file to: ",shutil.move(str(select_extension),PATH_SRC + file_type))
            time.sleep(1)
            
print("\nFiles moved successfully")

