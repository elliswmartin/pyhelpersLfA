# pyhelpersLfA
A series of python helpers to aid in file management and processing at Letterform Archive. 
 
## moveFromSubfolders.py

### How It Works
This script uses python to move files from the immediate subdirectories into the main directory. This script is not fully recursive, files will only be pulled from one level down into the main directory.  

It is meant to be used on its own or as an antidote to another LfA script, `moveJPGstofoldersHere.py` which organizes image files into new and existing subfolders based on work id (collection identification number). 

### Usage
1. Copy `moveFromSubfolders.py` into the main directory that you would like files to be moved to. 

2. Open Terminal and run `moveFromSubfolders.py`. 
      
        $ python3 /PATH/TO/FILES/moveFromSubfolders.py 

## Background 
I developed these scripts while working at Letterform Archive in San Francisco, CA to assist with automating small tasks. 
