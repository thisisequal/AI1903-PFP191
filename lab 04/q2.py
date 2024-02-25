def write_new(fname, content):
    with open(fname, 'w') as file:
        file.write(content)

def write_existing(fname, content):
    with open(fname, 'w') as file:
        file.write(content)

def write_list(fname, lst):
    with open(fname, 'w') as file:
        for line in lst:
            file.write(f"{line}\n")
        

def read_file(fname):
    with open(fname, 'r') as file:
        for line in file.readlines():
            print(line.strip())
    
path = "./Lab04/a/"
filename = "q2.txt"
filename_lst = "q2_lst.txt"

write_new(path + filename, "This is new content")
print("Done writing")
read_file(path + filename)

write_existing(path + filename, "This is overwritten content")
print("Opening file again..")
read_file(path + filename)

lst = ['Name: Emma', 'Address: 221 Baker Street', 'City: London']
write_list(path + filename_lst, lst)
print("Done writing list")
read_file(path + filename_lst)