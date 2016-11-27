
import os
import sys
currentPath = os.getcwd()
path= currentPath[:-7]
path =path+"/recommend/"
print("path now:"+path)

for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        if file[-2:] == "py":
            pathToFetch=dirpath+file
            command="radon cc -s "+pathToFetch 
            os.system(command)

    