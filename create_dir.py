'''The new_directory function creates a new directory inside the current working directory, 
then creates a new empty file inside the new directory, and returns the list of files in that directory.
 Complete the function to create a file "script.py" in the directory "PythonPrograms".'''
import os

def new_directory(directory, filename):
    if os.path.isdir(directory) is True:
        print('directory exists')
    else:
        os.makedirs(directory)
    os.chdir(directory)
    with open(filename,'w+') as file:
        pass
    return (os.listdir())
  
print(new_directory("PythonPrograms", "script.py"))