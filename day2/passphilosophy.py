# Part 1
count = 0
with open("D:\\Coding\\AdventofCode\\day2\\input.txt", "r") as f:
    for line in f:
        interval, char, password = line.strip().split()
        num1, num2 = map(int, interval.split("-"))
        if password.count(char[0]) >= num1 and password.count(char[0]) <= num2:
            count += 1
print(count)

# Part 2
count2 = 0
with open("D:\\Coding\\AdventofCode\\day2\\input.txt", "r") as f:
    for line in f:
        interval, char, password = line.strip().split()
        num1, num2 = map(int, interval.split("-"))
        if password[num1 - 1] == char[0] and password[num2 - 1] != char[0]:
            count2 += 1
        elif password[num1 - 1] != char[0] and password[num2 - 1] == char[0]:
            count2 += 1
print(count2)