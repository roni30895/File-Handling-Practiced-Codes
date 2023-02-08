# program to change file permission
import os
import sys
import stat

def file_permission_change():
    os.chmod("12_copy_intra_machine.py", stat.S_IREAD)
    print("Only owner can read this file")

    # Setting the given file to be read by group.
    os.chmod("12_copy_intra_machine.py", stat.S_IRWXU )
    print("Now, file permissin got changed,owner can read,write and execute the file.")
file_permission_change()