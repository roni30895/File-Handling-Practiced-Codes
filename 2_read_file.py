# 2.Write a function to read an existing text file and display its contents in terminal

def read():
    with open("questions.txt","r") as f:
        for line in f:
            print(line)
read()