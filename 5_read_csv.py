# Write a function to read csv file and display data on terminal.
import pandas as pd
def read_csv(): 
    dataframe1 = pd.read_csv('data.csv')
    print(dataframe1)
read_csv()