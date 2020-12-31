import csv

with open('birthdays.csv', 'a', newline='') as f:
    dateName = ['name', '03.04.2123']
    csvWriter = csv.writer(f)
    csvWriter.writerow(dateName)
     
with open('birthdays.csv', 'rt') as f:
    csvReader = csv.reader(f)
    for p in csvReader:
        print(p[0])

