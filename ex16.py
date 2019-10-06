from sys import argv

script, filename = argv #filename should be given with extension

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CRTL-C(^C).")
print("If you do want that, hit RETURN.")

input("?") #pause for user's response

print("Opening the file ...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate() #clear the content in the file just created

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

#target.write(line1)
#target.write("\n") #break the line or start a new line
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write("{}\n{}\n{}".format(line1, line2, line3))

print("Check the file before we close it:")
print("line1: {}\nline2: {}\nline3: {}".format(line1, line2, line3))

input("Press enter to close the file")

print("And finally, we close it.")
target.close() #it's a good practice always closing a file at the end
