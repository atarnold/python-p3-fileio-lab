def write_file(file_name, file_content):
    my_file = open(f"{file_name}.txt", mode='w')
    my_file.write(file_content)
    my_file.close()

def append_file(file_name, append_content):
    my_file = open(f"{file_name}.txt", 'a')
    my_file.write(append_content)
    my_file.close()

def read_file(file_name):
    fhandle = open(f"{file_name}.txt")
    return fhandle.read()