#os module in python provides functions for interacting with the operating system
 
import os
#get the current working directory
cwd=os.getcwd()
print(cwd)
#output is C:\Users\Dell\Desktop\class99

#os.chdir()is used to change the cwd to a specified path

os.chdir('C:/Users/Dell/Desktop/class99')
cwd=os.getcwd()
print(cwd)

#creating a directory 
#os.mkdir('myfolder')

#makedirs() will create a directory recursively

#os.makedirs('folderA/folderB')

#listdir(path) is used to list all the files and folder under that path 
dir_list=os.listdir('C:/Users/Dell/Desktop/class99')
print('files and directories in',dir_list)

#removing file
#os.remove('sample1.txt')

#deleting directory
#os.rmdir('myfolder')

#os.name gives the name of the operating system
print(os.name)

import mymodule
print(mymodule.person1)
print(mymodule.greeting("Kavya"))
print(mymodule.greeting("Dev"))