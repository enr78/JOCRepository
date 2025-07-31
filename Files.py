# Day 5: Portfolio Practice - Files - Storing Data and calling it from other files
# Create a program that reads in each line of the file, and prints "Hello, ..."

filename = "hello.txt"  # file path, in this case just the file name because the file is in the same location as this file 'Files.py'
fileHandle = open(
    filename
)  # above won't work without this line. This is the file handle. It can be called anything you like
output = open("output.txt", "w")
for line in fileHandle:
    print(
        "Hello, " + line.rstrip() + "!", file=output
    )  # rstrip removed the by the print function
print()

fileHandle.close()
########## Below is another way of opening the same file with less code
for line in open(
    "hello.txt"
):  # fileHandle doesn't need to be closed here becuse it inherently closes at the end of the for loop
    print("Hello,", line.strip() + "!")
