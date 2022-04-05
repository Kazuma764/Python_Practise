flag = True
list = []
count = 0

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

for k in range(len(list)):
    count = 0
    for l in range(list[k][0]):
        count = 0
        if l != 0:
            print("")
        for m in range(list[k][1]):
            if l%2 ==0:
                if count%2 == 0:
                    print("#", end='')
                else:
                    print(".", end='')
            elif l%2 !=0:
                if count%2 == 0:
                    print(".", end='')
                else:
                    print("#", end='')
            count +=1
        
    print()
    print()


"""
count = 0

for i in range(6):
    count = 0
    if i != 0:
        print("")
    for k in range(6):
        if i%2 ==0:
            if count%2 == 0:
                print("#", end='')
            else:
                print(".", end='')
        elif i%2 !=0:
            if count%2 == 0:
                print(".", end='')
            else:
                print("#", end='')
        count +=1
"""
  

   