import csv
import pandas as pd



with open('/Users/ishanpathak/Desktop/Workshop-foundation-of-data-science/college-workshop-FDS/sem5pract2new.csv' , mode='r') as file:
    csvFile=csv.reader(file)

df=pd.read_csv('sem5pract2new.csv',encoding="latin-1",error_bad_lines=False)
print(df)