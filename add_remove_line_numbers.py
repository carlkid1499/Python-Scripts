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
        f = open(file,"r") # see for more information: https://www.w3schools.com/python/python_file_handling.asp
        #Note f is the file pointer
        print("Original File: \n")
        print(f.read())
        f.close()
        print("Adding line numbers...\n")
        # reference material for code below
        # https://docs.python.org/2/tutorial/inputoutput.html
        # https://docs.python.org/2/library/functions.html#enumerate
        with open(file, "r") as openfile:
            with open("test2.txt", "w") as outfile:
                for line_number, line in enumerate(openfile):
                    outfile.write('{0:<3}{1}'.format(line_number+1, line))
        f.close()
        f.close()

        f = open("test2.txt","r")
        print("\nModified File: \n")
        print(f.read())
        f.close()
        print("\n")
        
        
    elif (option == 2):
        file=input("Enter File Name: ") #read in the file name
        print("File name entered: ",file)
        print("Removing line numbers...\n")
        
        
    elif(option == 3):
        print("Exiting...\n")
        i = 1
    else:
        print("Invalid Option\n")
    
