import os, shutil, re
# this script works to undo the moveJPGstofoldersHere.py in case of error
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