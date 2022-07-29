from csv import reader
import os


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
                    distances.append(shortestdistance(roadlocations[i][0], roadlocations[i][1], travelled + [[currentrow, currentcol]], target))
                else:
                    distances.append(max(maxcol, maxrow) ** 2)
            return min(distances)


maplegend, matrix = {
    0: 'Road',
    1: 'House',
    2: 'Work',
}, []

for line in reader(open(os.path.join(os.sys.path[0], "Map.csv"))):
    lst = []
    for item in line:
        lst.append(int(item.strip()))
    matrix.append(lst)
del(line, lst, item)

# Adjusting values to index from 0 rather than 1

[row, col], maxcol, maxrow = map(lambda x: int(x) - 1, input("Matrix address: ").split()), len(matrix) - 1, len(matrix[0]) - 1
print(shortestdistance(row, col, [], 2))