import os
import shutil
from datetime import datetime

def rename_file(old, new):
    if os.path.exists(old):
        os.rename(old, new)
        print(f"{old} has been renamed to {new}")
    else:
        print(f"{old} does not exist.")

def rename_multiple(list, pref, path):
    list_new = []
    for i, fname in enumerate(list, start=1):
        name = f"{path}{pref}_{i}.txt"
        os.rename(fname, name)
        list_new.append(name)
    print("All files renamed")
    print("New names are")
    print(list_new)

def rename_in_folder(folder_path, pref):
    list = os.listdir(folder_path)
    for i, fname in enumerate(list, start=1):
        if os.path.isfile(os.path.join(folder_path, fname)):
            name = f"{pref}_{i}.txt"
            os.rename(os.path.join(folder_path, fname), os.path.join(folder_path, name))

def rename_timestamp(list):
    for fname in list:
        name, extension = os.path.splitext(fname)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_new = f"{name}_{timestamp}{extension}"
        os.rename(fname, name_new)

def rename_extension(list, extension):
    for fname in list:
        name, _ = os.path.splitext(fname)
        name_new = f"{name}.{extension}"
        os.rename(fname, name_new)

def rename_and_move(path_old, path_new):
    if os.path.exists(path_old):
        shutil.move(path_old, path_new)
        print(f"{path_old} has been moved to {path_new}")
    else:
        print(f"{path_old} does not exist.")

path = "./Lab04/a/"
q4 = f"{path}q4.txt"
file = open(q4, 'w')
file.close()

fname1 = f"{path}sales1.txt"
file1 = open(fname1, 'w')
file1.close()
fname2 = f"{path}sales2.txt"
file2 = open(fname2, 'w')
file2.close()

rename_file(q4, f"{path}q4_new.txt")
rename_multiple([fname1, fname2], "sales", path)
rename_in_folder(f"{path}Q4/", "sales_new")
rename_timestamp([f"{path}sales20.txt"])
rename_extension(os.listdir(f"{path}Q4/"), "pdf")
rename_and_move(f"{path}expense.txt", f"{path}/Q4/expense.txt")