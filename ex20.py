from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
# read the first line and stops at the end of it
# return a '\n' also, meaning there will be a empty line printed

current_line = current_line + 1 # current_line += 1
print_a_line(current_line, current_file)
# read the second line and stops at the end of it

current_line = current_line + 1
print_a_line(current_line, current_file)
