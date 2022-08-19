flag = True
list1 = []
count = 0

while flag:
    x = input().split()
    if x[0] == "0" and x[1] == "0":
        break
    else:
        list1.append(x)

for i in range(len(list1)):
    for j in range(len(list1[i])):
        list1[i][j] = int(list1[i][j])

for k in range(len(list1)):
    count = 0
    for l in range(list1[k][0]):
        count = 0
        if l != 0:
            print("")
        for m in range(list1[k][1]):
            if l % 2 == 0:
                if count % 2 == 0:
                    print("#", end='')
                else:
                    print(".", end='')
            elif l % 2 != 0:
                if count % 2 == 0:
                    print(".", end='')
                else:
                    print("#", end='')
            count += 1

    print()
    print()
