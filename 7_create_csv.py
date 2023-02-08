# Write a function to create CSV file with content.
import csv

def write_csv():
    Salary = (["Sr.No","Name","Salary"],
        ["1",'Rohan', 33375],
        ["2",'Anuj', 34360],
        ["3",'Palkesh', 34360],
        ["4",'Shubham',34360],
        ["5",'Virendra', 33375])
    with open("Salary.csv","w",newline="") as f:
        write=csv.writer(f)
        write.writerows(Salary)

write_csv()
