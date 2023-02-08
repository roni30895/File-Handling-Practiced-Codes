# Write a function to read excel sheet file and display data on terminal
import pandas as pd
def read_xl(): 
    dataframe1 = pd.read_excel('demo.xls')
    print(dataframe1)
read_xl()