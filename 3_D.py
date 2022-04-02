x = input("Enter the number :")
y = x.split()
list = [int(i) for i in y]
a,b,c = list[0],list[1],list[2]
count = 0

for i in range(a, b+1):
    if c%i == 0:
        count += 1

print(count)

    


