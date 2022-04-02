list = []
flag = 1

"""
def so_list(l):
    for i in range(0, len(l)):
        yield l[i].sort()
"""


while flag == 1:
    x = input("Enter the number :")
    y = x.split()
    if y[0] == "0" and y[1] == "0":
        break
    else:    
        list.append(y)
        print(list)

#answer = so_list(list)

for i in range(0, len(list)):
        list[i].sort()

for j in range(0,len(list)):
    print(list[j])
