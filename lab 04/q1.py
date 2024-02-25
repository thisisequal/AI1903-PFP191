import os
import stat
from datetime import datetime

path = "./Lab04/a/"
readonly = stat.S_IREAD
readonly_other = stat.S_IROTH
write = stat.S_IWRITE
write_other = stat.S_IWOTH
execute = stat.S_IEXEC
execute_other = stat.S_IXOTH


def create_empty_file(fname):
    with open(fname, 'w') as file:
        pass
    print(f"created {fname}")

def create_file_datetime(path):
    current = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fname = f"{path}{current}.txt"
    with open(fname, "w") as file:
        pass
    print(f"created {fname}")

def create_file_permission(fname, permission):
    with open(fname, 'w') as file:
        os.chmod(fname, permission)
        file.write(f"This file's permisison: {permission}")
    print(f"created {fname} with permission: {permission}")

create_empty_file(f"{path}sales.txt")
create_file_datetime(path)
create_file_permission(f"{path}sample.txt", write)