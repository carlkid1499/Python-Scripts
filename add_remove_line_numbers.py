#Like BASH begin with the shabang #!
#!/usr/bin/env python3
import shutil # import stuff to copy files see: https://docs.python.org/3/library/shutil.html
import re
import os

# getting the current working directory
src_dir = os.getcwd()

# printing current directory
print(src_dir)

# while loop for execution
file = "" # variable for the file name
option = ""
i = 0
while(i !=1):
    print("1: Add Line Numbers")
    print("2: Remove Line Numbers")
    print("3: Exit\n")
    option = int(input("Enter Option: ")) #this converts the input into an int
    if(option == 1):
        file=input("Enter File Name: ") #read in the file name
        print("File name entered: ",file) # this is kinda like C
        # copying the files
        shutil.copyfile(file, 'copy_' + file) #copy src to dst
        f = open(file,"r") # see for more information: https://www.w3schools.com/python/python_file_handling.asp
        #Note f is the file pointer
        print("Original File: \n")
        print(f.read())
        f.close()
        print("\nAdding line numbers...\n")
        # reference material for code below
        # https://docs.python.org/2/tutorial/inputoutput.html
        # https://docs.python.org/2/library/functions.html#enumerate
        with open(file, "r") as openfile:
            with open('copy_' + file, "w") as outfile:
                for line_number, line in enumerate(openfile):
                    outfile.write('{0:<5}{1}'.format(line_number+1, line))
                    # {0:<num_spacing} insert number and spaces 1_____text
                    # Note: number takes up one space as well.

        f = open('copy_' + file,"r")
        print("\nModified File: \n")
        print(f.read())
        f.close()
        print("\n")
        # Now overwrite the original file... why keeps copieis lol
        shutil.move('copy_' + file, file)
        
        
    elif (option == 2):
        file=input("Enter File Name: ") #read in the file name
        print("File name entered: ",file)
        f = open(file,"r")
        print("Original File: \n")
        print(f.read())
        f.close()
        print("\nRemoving line numbers...\n")

        with open(file, "r") as openfile:
            with open('copy_' + file, "w") as outfile:
                for line in openfile:
                    line = re.sub(r'\b[0-9]','',line) # remove any number
                    # r'\b[0-9]' ... the "r" says we are entering a regex
                    # r'regex','replace with',string)
                    line = line.lstrip() # remove leading spaces
                    outfile.write(line) 
        f = open('copy_' + file,"r")
        print("\nModified File: \n")
        print(f.read())
        f.close()
        print("\n")

        # Now overwrite the original file... why keeps copieis lol
        shutil.move('copy_' + file, file)
        
    elif(option == 3):
        print("Exiting...\n")
        i = 1
    else:
        print("Invalid Option\n")
    
