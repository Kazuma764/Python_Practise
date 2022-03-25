A = input("Enter the number :")
B = A.split()
list = [float(i) for i in B]
W,H,x,y,r = list[0],list[1],list[2],list[3],list[4]

a1 = x + r
a2 = x - r
b1 = y + r
b2 = y - r

if a1<W and a2>0 and b1<H and b2>0:
    print("Yes")
else:
    print("No")