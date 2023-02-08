# Write a function to add text content to any existing file.

def append_txt(input):
    with open("simple.txt",'a') as f:
        
        f.write("\n"+ input)

input=input("\n Enter the text which you want to append in file : ")
append_txt(input)