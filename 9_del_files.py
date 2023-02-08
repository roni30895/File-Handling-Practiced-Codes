# Write a function to delete files or directories.
import os

def del_file():
    file='demo.txt'
    location="F:/Assignment By Rahul/7. File Handling/"
    path=os.path.join(location,file)
    os.remove(path)
del_file()
