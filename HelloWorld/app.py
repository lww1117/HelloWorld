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
    remNames = len(names) % x
    print(remNames)
    if remNames > 1:
        remNames = int(x / remNames)
    teamSize = len(names)/ x + remNames
    print(remNames)
    print(int(teamSize))
    while len(names) > teamSize:
        a = sample(names, int(teamSize))
        teams.append(a)
        for row in a:
            names.remove(row)
    for row in teams:
        print(row)
    print(names)
