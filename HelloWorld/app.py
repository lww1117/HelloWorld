import csv
from random import sample
names = []
teams = []

x = int(input("Select number of teams: "))

with open('spring-22-students.tsv', newline='') as file:
    iterator = csv.reader(file, delimiter='\t', quotechar='|')
    next(iterator, None)
    for row in iterator:
        names.append(row[0])
    while len(names) > x:
        a = sample(names, x)
        teams.append(a)
        for row in a:
            names.remove(row)
    for row in teams:
        print(row)
    print(names)
