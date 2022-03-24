import math

S = input("Enter the number :")
if S.isdecimal():
    y = float(S)
    h = math.floor(y/3600)
    m = math.floor((y/60)%60)
    s = math.floor(y%60)

    print(f"{h}:{m}:{s}")
else:
    print("We cannot calculate")


