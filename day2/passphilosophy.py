# input_file = open("D:\\Coding\\AdventofCode\\day2\\input.txt", "r")
# inputdata = input_file.read()  # .splitlines()

count = 0
with open("D:\\Coding\\AdventofCode\\day2\\input.txt", "r") as f:
    for line in f:
        interval, char, password = line.strip().split()
        num1, num2 = map(int, interval.split("-"))
        if password.count(char[0]) >= num1 and password.count(char[0]) <= num2:
            count += 1

print(count)
# gonna try using something like grep