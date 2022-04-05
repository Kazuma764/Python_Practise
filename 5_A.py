flag = True
list = []

while flag == True:
    x = input("Enter the number :")
    y = x.split()
    if y[0] == "0" and y[1] == "0":
        break
    else:    
        list.append(y)

for i in range(len(list)):
    for j in range(len(list[i])):
        list[i][j] = int(list[i][j])

for l in range(len(list)):
    for j in range(list[l][0]):
        if j != 0:
            print("")
        for k in range(list[l][1]):
            print("#", end='')
        
    print()
    print()

