import csv 

with open('r', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)