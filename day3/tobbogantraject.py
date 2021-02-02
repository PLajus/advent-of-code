my_file = open("D:\\Coding\\AdventofCode\\day3\\input.txt", "r")
matrix = my_file.read().splitlines()

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
