# Example of a Square Grid

size(101, 101)
for row in range(0, 100, 10):
    for column in range(0, 100, 10):
        square(row, column,  10)
        print(row, column)
