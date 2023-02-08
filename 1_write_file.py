# 1.	Write a function to create simple text file with some text content.

def write(input):
    with open("simple.txt",'w') as f:
        f.write(input)

input=input("\n Enter the text which you want to write in file : ")
write(input)