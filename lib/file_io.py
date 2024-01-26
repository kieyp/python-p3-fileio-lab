def write_file(file_name , file_content):
    with open( f'{file_name}.txt', 'w') as file:
        file.write(file_content)

# Example usage:
# write_file(file_name='example.txt', file_content='This is the content.')

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)

# Example usage:
# append_file(file_name='example.txt', append_content='This is additional content.')

def read_file(file_name):
    with open(f'{file_name}.txt', 'r') as file:
     return file .read()

# Example usage:
# content = read_file(file_name='example.txt')
# print(content)

