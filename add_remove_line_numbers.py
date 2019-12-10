#Like BASH begin with the shabang #!
#!/usr/bin/env python3

from shutil import copyfile # import stuff to copy files see: https://docs.python.org/3/library/shutil.html

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
        f = open(file,a
        print("Adding line numbers...\n")
    elif (option == 2):
        file=input("Enter File Name: ") #read in the file name
        print("File name entered: ",file)
        print("Removing line numbers...\n")
        
        
    elif(option == 3):
        print("Exiting...\n")
        i = 1
    else:
        print("Invalid Option\n")
    
