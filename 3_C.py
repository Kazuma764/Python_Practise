list = []
flag = True

while flag:
    x = list(map(int, input().split()))
    if x[0] == 0 and x[1] == 0:
        break
    else:    
        list.append(x)

#answer = so_list(list)

for i in range(len(list)):
        list[i].sort()

for j in range(0,len(list)):
    print(list[j])

