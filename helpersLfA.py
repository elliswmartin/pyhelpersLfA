import os, csv, re, shutil

# TODO - ask user input if press "m" then run moveFromSubfolders()
# if press "r" then run renamer()

print("This script allows you to do multiple python tasks in one!\n Press 'e' for renamer.py\n Press 's' for moveFromSubfolders.py\n Press 'q' to quit.")
inpt = input("Please make a selection:")
inpt = inpt.lower() 

def moveFromSubfolders():
    # this function works to undo the moveJPGstofoldersHere.py in case of error
    # by moving all files within one level of subdirectories back into the main directory.  

    # create list of all subdirectories (1 level down only)
    folders = next(os.walk('.'))[1]
    destination = os.getcwd() + '/'

    # loop through subdirectories 
    for f in folders:
        os.chdir(destination + f)
        source = os.getcwd()
        files = os.listdir()
        # loop through files in fth subdirectory
        for file in files: 
            shutil.move(file, destination)	
        print("Files moved from " + str(f))
        os.chdir(source)

def renamer():

    os.chdir("/Users/ellis/Desktop/rename") 
    cwd = os.getcwd() + "/"
    nwd = cwd + "done/" # subdirectory to move renamed files into

    file = open('rename.csv')
    file = csv.reader(file)

    old_name = []
    new_name = []

    # create lists of old and new names from rename.csv
    for line in file:
        old_name.append(line[0]) 
        new_name.append(line[1])

    # create new subdirectory if does not already exist 
    if os.path.exists(nwd) == False: 
        os.makedirs(nwd)

    # loop through files in old_name list to rename      
    for file in old_name:
        index = old_name.index(file)

        # do not rename if file names are the same 
        if file == new_name[index]:
            print(file + " not renamed to " + new_name[index] + "\nOriginal and new filenames are the same.")
            shutil.move(cwd + file, nwd + file)
    
        # do not rename if new filename already exists in subfolder
        elif new_name[index] in os.listdir(nwd):
            print(file + " not renamed to " + new_name[index] + ".\nNew filename already exists in 'done' folder")
        
        # all clear to rename
        else:
            try: 
                shutil.copy(cwd + file, nwd + new_name[index])
                print("File renamed successfully.")
                os.remove(file) # remove file once renamed and moved 
            except: 
                print("Error occurred while renaming file.")

# continue to prompt user until they quit
while inpt != 'q':
    if inpt == 's' :
        moveFromSubfolders()
    elif inpt == 'e':
        renamer()
    else:
        print("invalid selection.")
        print("\n Press 'e' for renamer.py\n Press 's' for moveFromSubfolders.py\n Press 'q' to quit.")
    inpt = input("Please make a selection:")
    inpt = input.lower()
