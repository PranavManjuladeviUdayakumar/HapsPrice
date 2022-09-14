#Library/Module importing
from csv import reader
import os

#Function declarations
def getsurroundings(currentpyro, currentpycol, target=0):
    lst = []
    if currentpyro + 1 <= maxcol:
        if matrix[currentpyro + 1][currentpycol] == target:
            lst.append([currentpyro+1, currentpycol])
    if currentpyro - 1 >= 0:
        if matrix[currentpyro - 1][currentpycol] == target:
            lst.append([currentpyro-1, currentpycol])
    if currentpycol + 1 <= maxrow:
        if matrix[currentpyro][currentpycol+1] == target:
            lst.append([currentpyro, currentpycol+1])
    if currentpycol - 1 >= 0:
        if matrix[currentpyro][currentpycol-1] == target:
            lst.append([currentpyro, currentpycol-1])
    return lst


def shortestdistance(currentrow, currentcol, travelled, target=2):
    if len(getsurroundings(currentrow, currentcol, target)) != 0:
        return len(travelled)
    else:
        roadlocations = getsurroundings(currentrow, currentcol, 0)
        roads = len(roadlocations)
        if roads == 0:
            return max(maxcol, maxrow) ** 2
        else:
            distances = []
            for i in range(roads):
                if [roadlocations[i][0], roadlocations[i][1]] not in travelled:
                    distances.append(shortestdistance(
                        roadlocations[i][0], roadlocations[i][1], travelled + [[currentrow, currentcol]], target))
                else:
                    distances.append(max(maxcol, maxrow) ** 2)
            return min(distances)


def houseprice(workdistance, hospitaldistance, malldistance):
    return Baseprice + workdistance * Workmultiplier + hospitaldistance * Hospitalmultiplier + malldistance * Mallmultiplier


#App beginning
#Variable declarations
matrix = []
longtext = '''
HapsPrice instructions-

Enter the name of csv file (in the same directory) to be used as a map. Eg. Map
Enter house address as 2 integers separated by a space. Eg. 8 1
House price modifiers can be modified through a y/n prompt.
Details of the price of a house, read from a MySQL database, can be chosen to be displayed after price prediction.
Any errors in input will require the whole program to be re-executed.
'''
print(longtext)

#Matrix setup
Matrixlegend = {
    0: "Road",
    1: "House",
    2: "Work",
    3: "Hospital",
    4: "Mall"
}
print("Matrix legend is", Matrixlegend)
Map = input("CSV file: ")
for line in reader(open(os.path.join(os.sys.path[0], f"{Map}.csv"))):
    lst = []
    for item in line:
        lst.append(int(item.strip()))
    matrix.append(lst)
del(line, lst, item)

# Adjusting values to index from 0 rather than 1
[row, col], maxcol, maxrow = map(lambda x: int(
    x) - 1, input("House Location: ").split()), len(matrix) - 1, len(matrix[0]) - 1

#Price Settings
Baseprice = 17000
Workmultiplier = -150
Hospitalmultiplier = -125
Mallmultiplier = -100
cons1, cons2 = "Edit? (y/n): ", "Enter new integer value: "
if input("Edit Price modifiers? (y/n): ").lower() == 'y':
    print(f"Base price for every house = {Baseprice}")
    if input(cons1).lower() == 'y':
        Baseprice = int(input(cons2))
    print(f"Work multiplier for every house = {Workmultiplier}")
    if input(cons1).lower() == 'y':
        Workmultiplier = int(input(cons2))
    print(f"Hosptial multiplier for every house = {Hospitalmultiplier}")
    if input(cons1).lower() == 'y':
        Hospitalmultiplier = int(input(cons2))
    print(f"Mall multiplier for every house = {Mallmultiplier}")
    if input(cons1).lower() == 'y':
        Mallmultiplier = int(input(cons2))

#Price
work = shortestdistance(row, col, [], 2)
hospital = shortestdistance(row, col, [], 3)
mall = shortestdistance(row, col, [], 4)
print("Distances: ", work, hospital, mall)
print("House Price with current modifiers is: ",
      houseprice(work, hospital, mall))

#MySQL extraction
if input("Retrieve house information from MySQL? (y/n): ").lower() == 'y':
    print('haha')
