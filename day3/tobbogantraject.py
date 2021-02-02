import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'input.txt')

my_file = open(filename, "r")
matrix = my_file.read().splitlines()
my_file.close()

def tree_count(right, down):
    trees = 0
    line = 0
    position = 0
    while line < len(matrix):
        if matrix[line][position] == "#":
            trees += 1 
        line += down
        position += right
        if (position > len(matrix[0])-1):
            position -= len(matrix[0])
    return trees

#part 1
print(tree_count(3, 1))
#part 2
print(tree_count(1,1)*tree_count(3,1)*tree_count(5,1)*tree_count(7,1)*tree_count(1,2))