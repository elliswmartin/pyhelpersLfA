# pyhelpersLfA
A series of python helpers to aid in file management and processing at Letterform Archive. 
 
# moveFromSubfolders.py

### How It Works
This script uses python to move files from the immediate subdirectories into the main directory. This script is not fully recursive, files will only be pulled from one level down into the main directory.  

It is meant to be used on its own or as an antidote to another LfA script, `moveJPGstofoldersHere.py` which organizes image files into new and existing subfolders based on work id (collection identification number). 

### Usage
1. Copy `moveFromSubfolders.py` into the main directory that you would like files to be moved to. 

2. Open Terminal and run `moveFromSubfolders.py`. 
      
        $ python3 /PATH/TO/FILES/moveFromSubfolders.py 

# helpersLfA.py

### How It Works
___________ 
 

### Usage (Mac Only) 

1. This script only requires a specific folder structure for the `rename` function. 

2. Open Terminal and run `helpersLfA.py`: 

        $ python3 /PATH/TO/SCRIPT/helpersLfA.py 

4. When prompted, enter a character in Terminal based on the process you would first like to run (see below for more details on the selections).  

5. Continue to select a process until you would like to quit. 

### How It Works
A combination of all of the scripts above with command line user input to customize each script execution. 

The script continues to prompt the user until "q" character is pressed: 

```  
if inpt == 's':
    moveFromSubfolderstest()
elif inpt == 'r':
    renamertest()
else:
    print("invalid selection.")
    print("\n Press 'r' for renamer.py\n Press 's' for moveFromSubfolders.py\n Press 'q' to quit.")
inpt = input("Please make a selection:")
```

Each letter corresponds to a different process, of which the code is copied exactly from the 2 scripts above and [autocrop](https://github.com/elliswmartin/autocropLfA/blob/85c9591d4c998e8d62e71494234da52d38808b6a/autocrop.sh): 

* `s`: Tifs in `crop` folder are turned into jpgs.
* `e`: Jpgs in `OA_process` folder are resized to 3000px on longest side, and mid files are created (800px copies of orig files)    
* `q`: Quits the script. 


# Background 
I developed these scripts while working at Letterform Archive in San Francisco, CA to assist with automating small tasks. 
