import csv
from random import sample

names = []
teams = []

numTeams = int(input("Select number of teams: "))

with open('spring-22-students.tsv', newline='') as file:
    iterator = csv.reader(file, delimiter='\t', quotechar='|')
    next(iterator, None)
    for row in iterator:
        names.append(row[0])
    remNames = len(names) % numTeams
    teamSize = len(names)/ numTeams
    while len(names) > teamSize:
        if remNames != 0:
            remNames -= 1
            addName = sample(names, int(teamSize) + 1)
            teams.append(addName)
            for row in addName:
                names.remove(row)
        else:
            addName = sample(names, int(teamSize))
            teams.append(addName)
            for row in addName:
                names.remove(row)
    for row in teams:
        print(row)
    print(names)
