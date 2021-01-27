my_file = open("D:\\Coding\\.vscode\\day1\\input.txt", "r")
datalist = my_file.read().split()
datalist = list(map(int, datalist))
my_file.close()

# Part 1
for i in range(0, len(datalist) - 1):
    for j in range(i + 1, len(datalist)):
        if datalist[i] + datalist[j] == 2020:
            print(datalist[i] * datalist[j])
            break

# Part 1 better solution
# s = set()
# for i in range(len(datalist)):
#  if 2020 - int(datalist[i]) in s:
#      print(int(datalist[i]) * (2020 - int(datalist[i])))
#      break
#  s.add(int(datalist[i]))

# Part 2
for i in range(len(datalist)):
    for j in range(i + 1, len(datalist)):
        if 2020 - (datalist[i] + datalist[j]) in datalist:
            print(datalist[i] * datalist[j] * (2020 - (datalist[i] + datalist[j])))
            break
