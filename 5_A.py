flag = True
list1 = []

while flag:
    x = input().split()
    if x[0] == "0" and x[1] == "0":
        break
    else:
        list1.append(x)

for i in range(len(list1)):
    for j in range(len(list1[i])):
        list1[i][j] = int(list1[i][j])

for l in range(len(list1)):
    for j in range(list1[l][0]):
        if j != 0:
            print("")
        for k in range(list1[l][1]):
            print("#", end='')

    print()
    print()
