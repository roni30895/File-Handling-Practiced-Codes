# Write a function to create a excel worksheet file with content.

import xlsxwriter
def write_xl():
    with open("Salary.xlsx","w") as f:
        pass
    file= xlsxwriter.Workbook('Salary.xlsx')
    worksheet = file.add_worksheet("My worksheet")
    Salary = (["Name","Salary"],
        ['Rohan', 33375],
        ['Anuj', 34360],
        ['Palkesh', 34360],
        ['Shubham',34360],
        ['Virendra', 33375])
    row = 1
    col = 1
    for name, salary in (Salary):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, salary)
        row += 1
    file.close()

write_xl()