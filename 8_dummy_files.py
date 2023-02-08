# Write a function to generate dummy files? Create large dummy / test files / directories with data size 1 to 10 GB.
import os
def generate_dummy_file(file_name, size_in_gb):
    # convert GB to bytes
    size = int(size_in_gb * 1024 * 1024 * 1024) 
    with open(file_name, "wb") as f: # wb indicates that the file is opened for writing in binary mode
        
        f.write(os.urandom(size)) # os.urandom() function  will genrate the random data

if __name__=="__main__":
    file_name=input("\n Enter file name with extension : ")
    size_in_gb=int(input("\n Enter the size of the file in GB : "))
    generate_dummy_file(file_name,size_in_gb)