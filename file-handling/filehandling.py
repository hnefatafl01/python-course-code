# r opens for reading only, pointer is placed at the beginning of the file. this is default mode
# r+ opens a file for both reading and writing. The file pointer is placed at the beginning of the file.
# w Opens a file for writing only. Overwrites the file if it exists.If the file doesn't exist, creates a new file
# w+  opens a file for both reading and writing. Overwrites the file if it exists.If the file doesn't exist, creates a new file
# a opens a file for appending. The file pointer is at the end if it exists. If file doesn't exist creates a new one for writing.
# a+ Opens a file for both appending and reading.Pointer at end if exists. file opens in append mode. If file nonexistant, creates new one for reading and writing.


# read files

# file=open("./files/example.txt",'r')
# print(type(file))
# content=file.read()
# content=file.readlines()
# print(content)
# file.seek(0)
# content1=[i.rstrip("\n") for i in content]
# print(content1)
# file.close()

#write files
## cannot write multiple lines without executing multiple times with \n using write method
# file=open("example2.txt",'w')
# file.write("show me the moneys")
# file.close()


# file2=open("example1.txt",'w')
# text = ["show","me","the","moneys"]
# for word in text:
#     file2.write(word + "\n")
# file2.close()

#appending
# file=open("example2.txt",'a')
# file.write("Line 4")
# file.close()

# with
with open("example.txt","a+") as file:
    file.seek(0)
    content=file.read()
    file.write("\nLine 6")
content
