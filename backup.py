#Like BASH begin with the shabang #!
#!/usr/bin/env python3

import datetime # Lets get that time
import os # gets funtions for os stuff like making directories
import tarfile # tar stuff to zip files
import shutil
backupdir = ""

timedate = str(datetime.date.today()) # just the date
timehour = str(datetime.datetime.today().hour) # just the hour 
timemin = str(datetime.datetime.today().minute) # just the min
timesec = str(datetime.datetime.today().second) # just the sec
timestamp = timedate + '-' + timehour + '-' + timemin + '-' + timesec # combine them

response = ""
response = input("Enter - folder/file,destination Note: must be seperated by comma: ")
inputlist = response.split(",") # split up string into a list of items.

backupdir = inputlist[1] + "\.backup"

if os.path.isdir(backupdir):
    print("\nDirectory exists backing up to: ",backupdir)
else:
    os.mkdir(backupdir) # make the back up dir
    print("\nDirectory created: ",backupdir)

foldercounter = 0
filecounter = 0
with tarfile.open('backup-' + timestamp + '.tar.gz', "w:gz") as tar_handle: #create the tar file
    for root, dirs, files in os.walk(inputlist[0]): # walk the dir/file to be backuped up
        foldercounter += 1
        for file in files: # walk all files and folders
            tar_handle.add(os.path.join(root, file)) # add the stuff to the tar file
            filecounter += 1 # counter
            
    if(foldercounter == 0 and filecounter == 0): # single file case
        tar_handle.add(inputlist[0]) # add the stuff to the tar file
        filecounter += 1 # counter
            
shutil.move('backup-' + timestamp + '.tar.gz',backupdir) # move tar file into the backupdir
            
print("\nFiles: ",filecounter,"Folders: ",foldercounter)

            

    
    
    


