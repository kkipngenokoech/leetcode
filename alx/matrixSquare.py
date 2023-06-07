#!/usr/bin/python3

print('Hello multiverse')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
matrixcopy = [row[:] for row in matrix]
for row in matrixcopy:
    for index, col in enumerate(row):
        row[index] = col*col
print(matrixcopy, matrixcopy, matrix)
