import os, csv, re, shutil
from PIL import Image

print('''
    This script allows you to do multiple python tasks in one!\n
        Press 's' for moveFromSubfolders.py\n
        Press 'e' for renamer.py\n
        Press 'h' for moveJPGstofoldersHere.py\n
        Press 'c' for createImagesList.py\n
        Press 'q' to quit.
        ''')
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

def moveJPGstofoldersHere():

    # this reads the folder it's in folder
    # then takes the first part of the file name eg lfa_emigre_0096 (not the image bit) by finding the first numeric character and allowing for the 4digit id
    # then uses that to create a folder if not existing and finally moves the image to that folder (makes sure all are lower case names)
    

    for f in os.listdir():
        if '.jpg' in f:
            m = re.search(r"\d", f)

            folderName = f[0:(m.start()+4)].lower()

            print (folderName)
        
            if not os.path.exists(folderName):
                os.mkdir(folderName)
                shutil.move(os.path.join('', f.lower()), folderName)
            else:
                shutil.move(os.path.join('', f.lower()), folderName)

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))]

def createImagesList():
    # this function creates imgdimensions.csv TODO improve this description

    savePath = 'imgdimensions.csv'
    imgcvsexists = os.path.exists(savePath)
    print(imgcvsexists)
    d = os.getcwd()
    itemFs = get_immediate_subdirectories(d)
    if imgcvsexists:
        os.remove(savePath)
    for folder in itemFs:
        print('checking ' + folder)
        for filename in os.listdir(folder):
            if filename.endswith("_mid.jpg") and re.search('.*\.\_.*', filename) == None:
                fid = os.path.join(folder, filename)
                mtime = os.path.getmtime(fid)
                ctime = os.path.getctime(fid)
                print("fid === " + fid)
                # with Image.open(fid) as im:
                im = Image.open(fid)
                width, height = im.size
            ##	print([folder, filename, width, height])

                with open(savePath, 'a') as csvfileO:
                    spamwriter = csv.writer(csvfileO, delimiter=','
                        )
                    spamwriter.writerow([folder, filename, width, height, mtime, ctime]) 

    print('done')

# continue to prompt user until they quit
while inpt != 'q':
    if inpt == 's' :
        moveFromSubfolders()
    elif inpt == 'e':
        renamer()
    elif inpt == 'h':
        moveJPGstofoldersHere()
    elif inpt == 'c':
        createImagesList()
    else:
        print("Invalid selection.")
    print('''
         Press 's' for moveFromSubfolders.py\n
         Press 'e' for renamer.py\n
         Press 'h' for moveJPGstofoldersHere.py\n
         Press 'c' for createImagesList.py\n
         Press 'q' to quit.
         ''')
    inpt = input("Please make a selection:")
    inpt = input.lower()
