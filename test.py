def so_list(l):
    for i in range(0, len(l)):
        l[i].sort()

list = [[5,4],[3,2],[7,6]]
so_list(list)
print(list)