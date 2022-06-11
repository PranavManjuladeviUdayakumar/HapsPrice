import csv
import os


matrix = []
maplegend = {
    0: 'Road',
    1: 'House',
    2: 'Work',
}

with open(os.path.join(os.sys.path[0], "Map.csv"), "r") as file:
    csvfile = csv.reader(file)

    i = 0

    for line in csvfile:
        lst = []
        for item in line:
            lst.append(int(item.strip()))
        matrix.append(lst)

print(matrix)

# Math matrix - Index begins from 1; Python matrix - Index begins from 0

[mathrow, mathcol] = map(int, input("Math matrix address: ").split())

# Convert Math index to Python index
pyro, pycol = mathrow - 1, mathcol - 1


print(pyro, pycol)
print(matrix[pyro][pycol])
pycolumnsmax, pyrowsmax = len(matrix) - 1, len(matrix[0]) - 1


def getsurroundings(currentpyro, currentpycol, target=0):
    lst = []
    if currentpyro + 1 <= pycolumnsmax:
        if matrix[currentpyro + 1][currentpycol] == target:
            lst.append([currentpyro+1, currentpycol])
    if currentpyro - 1 >= 0:
        if matrix[currentpyro - 1][currentpycol] == target:
            lst.append([currentpyro-1, currentpycol])
    if currentpycol + 1 <= pyrowsmax:
        if matrix[currentpyro][currentpycol+1] == target:
            lst.append([currentpyro, currentpycol+1])
    if currentpycol - 1 >= 0:
        if matrix[currentpyro][currentpycol-1] == target:
            lst.append([currentpyro, currentpycol-1])
    return lst


def shortestdistance(currentpyro, currentpycol, target=2, locationstraversed=[]):
    if len(getsurroundings(currentpyro, currentpycol, target)) != 0:
        return len(locationstraversed)
    else:
        roadlocations = getsurroundings(currentpyro, currentpycol, 0)
        roads = len(roadlocations)
        if roads == 0:
            return 9**9
        else:
            distances = []
            locationstraversed.append([currentpyro, currentpycol])
            for i in range(roads):
                if [roadlocations[i][0], roadlocations[i][1]] not in locationstraversed:
                    distances.append(shortestdistance(
                        roadlocations[i][0], roadlocations[i][1], target, locationstraversed))
                else:
                    distances.append(9**9)
            return min(distances)


print(shortestdistance(pyro, pycol, 2, []))
