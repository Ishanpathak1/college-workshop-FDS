import csv
from unittest import skip
import pandas as pd



with open('/Users/ishanpathak/Desktop/Workshop-foundation-of-data-science/college-workshop-FDS/sem5pract2new.csv' , mode='r') as file:
    csvFile=csv.reader(file)

df=pd.read_csv('sem5pract2new.csv',names=['Name','Enrolment Number', 'Semester','Percentage'],
  usecols=['Name'],skiprows=[0,1,2])
print(df)