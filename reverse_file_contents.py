# Carlos Santos
# CS 270
# Bruce Bolden
# 12/13/19
# A script to reverse the contents of a file

#Like BASH begin with the shabang
#!/usr/bin/env python3
import shutil # import stuff to copy files see: https://docs.python.org/3/library/shutil.html


i = 0
while(i != 1):
    print("\n\n1: Run")
    print("2: Exit")
    option = int(input("Enter Option: "))
    if(option ==1):


        filename = input("Enter  File Name: ")
        with open(filename, "r") as openfile:
            inputlist = openfile.read().splitlines() # read lines from a file and import into a list. Also split the strings
            openfile.close() # close the file.

        with open('backwards' + filename, "w") as outfile:
            inputlist.reverse() # reverse the list
            listsize = len(inputlist) # get the size of the list
            for i in range(0,listsize):
                outfile.write(inputlist[i]) # write list items
                outfile.write("\n") # write a new line after the item
            outfile.close() # close the file
        print("Reversing file...\n\n")
         # Now overwrite the original file... why keeps copiess lol
        shutil.move('backwards' + filename, filename)

        f = open(filename,"r")
        print("Modified File: \n")
        print(f.read())
        f.close()


    elif(option == 2):
        i = 1
    else:
        print("Invalid Option")