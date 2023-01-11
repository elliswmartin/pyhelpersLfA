# pyhelpersLfA
A series of python helpers to aid in file management and processing at Letterform Archive. 
 
# moveFromSubfolders.py

### How It Works (Mac Only)
This script uses python to move files from the immediate subdirectories into the main directory. This script is not fully recursive, files will only be pulled from one level down into the main directory.  

It is meant to be used on its own or as an antidote to another LfA script, `moveJPGstofoldersHere.py` which organizes image files into new and existing subfolders based on work id (collection identification number). 

### Usage
1. Copy `moveFromSubfolders.py` into the main directory that you would like files to be moved to. 

2. Open Terminal and run `moveFromSubfolders.py`. 
      
        $ python3 /PATH/TO/FILES/moveFromSubfolders.py 

# helpersLfA.py

### How It Works
A combination of all of the scripts above with command line user input to customize each script execution. 

The script continues to prompt the user until "q" character is pressed: 

```  
if inpt == 's':
    moveFromSubfolders()
elif inpt == 'r':
    renamer()
else:
    print("invalid selection.")
    print("\n Press 'r' for renamer.py\n Press 's' for moveFromSubfolders.py\n Press 'q' to quit.")
inpt = input("Please make a selection:")
```

Each letter corresponds to a different process, of which the code is copied exactly from the 2 scripts above and [autocrop](https://github.com/elliswmartin/autocropLfA/blob/85c9591d4c998e8d62e71494234da52d38808b6a/autocrop.sh): 

* `s`: Move files from workID-specific subfolders into main directory. 
* `e`: Bulk rename files in `rename` folder using `rename.csv` for file-level control.   
* `h`: Nest files into subfolders by workID. 
* `c`: Create image dimension list.  
* `q`: Quits the script. 

### Usage (Mac Only) 

1. Prepare files according to whichever process you would like to run. See above for moveFromSubfolders and [renamer](https://github.com/elliswmartin/renamer/blob/4e10206972eec4e69fb1337b42785befd60cd243/renamer.py) for rename. 

2. Open Terminal and run `helpersLfA.py`: 

        $ python3 /PATH/TO/SCRIPT/helpersLfA.py 

4. When prompted, enter a character + `enter` in Terminal based on the process you would first like to run.

5. Continue to select a process until you would like to quit. 

# Background 
I developed some of these scripts while working at Letterform Archive in San Francisco, CA to assist with automating small tasks. The functions createImageDimensions, get_immediate_subdirectories, and moveJPGstofoldersHere were written by [Murray Grigo-McMahon](https://www.paperposts.me) for LfA. 

