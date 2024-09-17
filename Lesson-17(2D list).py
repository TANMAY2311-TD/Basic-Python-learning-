matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

print(matrix[0])
print(matrix[1])
print(matrix[2])

print(matrix[1][1])
print(matrix[2][2])

matrix[2][0] = 10
print(matrix)

#using nested for loop
for row in matrix:
    for item in row:
        print(item)

for column in matrix:
    for item in column:
        print(item)
