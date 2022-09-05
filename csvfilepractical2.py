import csv

with open('/Users/ishanpathak/Desktop/Workshop-foundation-of-data-science/college-workshop-FDS/sem5pract2new.csv' , mode='r') as file:

    csvFile=csv.reader(file)

    for lines in csvFile:
        print(lines)