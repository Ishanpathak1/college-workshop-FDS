import csv
path="/Users/ishanpathak/Desktop/Workshop-foundation-of-data-science/college-workshop-FDS/sem5pract2new.csv"
with open(path,'a') as file:
    header=['Name','Enrolment Number', 'Semester','Percentage']
    data=[['Iron Man','20C22058','4','78%'],['Spider Man','20C22059','4','88%'],['Hulk','20C22059','4','89%']]

    writer=csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)