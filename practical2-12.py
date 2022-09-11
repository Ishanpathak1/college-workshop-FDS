import csv
import pandas as pd



with open('/Users/ishanpathak/Desktop/Workshop-foundation-of-data-science/college-workshop-FDS/sem5pract2new.csv' , mode='r') as file:
    csvFile=csv.reader(file)
print("Before changing")
df=pd.read_csv('sem5pract2new.csv',names=['Name','Enrolment Number', 'Semester','Percentage'],nrows=5)
  
print(df)
def rename(name):
    if name=="Ishan Pathak":
        return "Ishan Dushyant Pathak"
    else:
        return name
rename("Ishan")

print("After Changing")
df=pd.read_csv('sem5pract2new.csv',names=['Name','Enrolment Number', 'Semester','Percentage'],
  converters={"Name":rename},nrows=5)
print(df)