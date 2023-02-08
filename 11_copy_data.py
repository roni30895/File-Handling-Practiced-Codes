# Write a function to copy data from one directory to another directory.
import shutil
def copy_file():
    with open("F:/Assignment By Rahul/7. File Handling/copied/copied_file.txt","w") as f:
        pass
    source_file_path="F:/Assignment By Rahul/7. File Handling/questions.txt"
    destination_file_path="F:/Assignment By Rahul/7. File Handling/copied/Copied_file.txt"
    shutil.copy(source_file_path,destination_file_path)
copy_file()