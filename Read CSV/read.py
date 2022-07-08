import csv

file = open("iata_airlines.csv")
csvreader = csv.reader(file)

code = "AA"

rows = []
for row in csvreader:
    rows.append(row)

for i in range(len(rows)):
    if(rows[i][0] == code):
        print(rows[i][1])

file.close()