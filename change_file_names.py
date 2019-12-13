# Carlos Santos
# CS 270
# Bruce Bolden
# 12/13/19
# A script to update file names like .cPp --> .cpp or .cpP --> .cpp or any permutation of .cpp

#Like BASH begin with the shabang
#!/usr/bin/env python3
import os # gets funtions for os stuff like making directories
import re # reg ex https://docs.python.org/2/library/re.html
import shutil
i = 0
while(i != 1):
    print("\n\n1: Run")
    print("2: Exit")
    option = int(input("Enter Option: "))
    if(option ==1):
        filetype = input("Enter File Extension (i.e .txt, .docx): ")
        print("Current Directory Contents...")
        currdir = os.getcwd() # get the current working directory
        currfilelist = os.listdir(currdir) # returns list
        print(os.listdir(currdir))
        listsize = len(currfilelist) # get the size of the list
        print("\n\n") # lets add some spacing to make things look nice

        for item in os.listdir(currdir):
            pre, ext = os.path.splitext(item) # split filename into pre and ext pre.ext ... https://docs.python.org/2/library/os.path.html
            if re.search(filetype,item):
                pass # skip the all lower case version
            elif re.search(filetype,item,flags=re.I): # re.search("key","string","optional flags"), NOTE: catches the rest
                # flags=re.I says to ignore case. It'll match upper,lower, or a mix.  https://docs.python.org/2/library/re.html
                #create proper file name with the filetype
                print("Found:",item)
                print("New File Name:",pre + filetype)
                shutil.copy(item,pre + "old" + filetype) # make a copy of the file
                os.remove(item) # remove original file
                shutil.move(pre + "old" + filetype,pre + filetype) # rename the file

        print("\nNew Directory Contents...")
        currdir = os.getcwd() # get the current working directory
        currfilelist = os.listdir(currdir) # returns list
        print(os.listdir(currdir))
        print("\n\n") # lets add some spacing to make things look nice


    
    elif(option ==2):
        i = 1
    
    else:
        print("Invalid option!")

