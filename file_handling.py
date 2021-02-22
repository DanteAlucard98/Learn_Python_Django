"""File Handling."""

# data = open('data.txt', 'r')

"""
with open('data.txt', 'r') as data:
    print(f'File name: {data.name}')
    print('Read:')
    print(data.read())
"""

"""
lines = ["This is line 1", "This is line 2", "This is line 3", "This is line 4"]
with open('data.txt', 'w') as data:
    for line in lines:
        data.write(line)
        data.write('\n')
"""

"""
lines = ["This is line 5", "This is line 6", "This is line 7"]
with open('data.txt', 'rb') as data:
    data_as_list = data.readlines()

data_as_list.insert(1, "This is between line 1 and 2\n")

with open('data.txt', 'wb') as data:
    data_as_str = "".join(data_as_list)
    # "This is line 1\nThis is line 2\nThis is line 3\n"
    data.write(data_as_str)

with open('data.txt', 'ab') as data:
    for line in lines:
        data.write(line)
        data.write('\n')
"""

lines = [b"This is line 5", b"This is line 6", b"This is line 7"]
with open('word.docx', 'rb') as data:
    data_as_list = data.readlines()

data_as_list.insert(1, b"This is between line 1 and 2\n")

with open('word.docx', 'wb') as data:
    for data_line in data_as_list:
        data.write(data_line)
    for line in lines:
        data.write(line)
        data.write(b'\n')

"""
Text file's modes:

w - Write
r - Read
a - Append
r+ - Read & Write
x - Creation Mode

Text file's modes:

wb - Write
rb - Read
ab - Append
rb+ - Read & Write
"""
