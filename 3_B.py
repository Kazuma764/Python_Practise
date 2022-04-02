list = []
flag = 1

while flag == 1:
    x = input("Enter the number :")
    if x == "0":
        break
    else:    
        list.append(x)
        print(list)

for i in range(len(list)):
    print("Case",i+1,":",list[i])
