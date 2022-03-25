x = input("Enter the number :")
y = x.split()
a,b = y[0],y[1]

if a < b:
    print(a,"<",b)
elif a > b:
    print(a,">",b)
else:
    print(a,"==",b)

