flag = True
list = []

while flag == True:
    X = input("Enter the fomula :")
    Y = X.split()
    a, b = int(Y[0]), int(Y[2])
    if Y[1] == "+":
        list.append(a+b)
    elif Y[1] == "-":
        list.append(a-b)
    elif Y[1] == "*":
        list.append(a*b)
    elif Y[1] == "/":
        list.append(a//b)
    if Y[1] == "?":
        break

[print(i) for i in list]