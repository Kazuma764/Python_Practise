n = int(input())
y = []
z = []
i = 0
room = [0]*10
memory = []

def room_list(s,t):
    for o in range(n):
        if y[o][0]== s+1 and y[o][1]== t+1:
            z.append(y[o])
    return z      

def calculate(u):
    for p in range(len(z)):
        a = z[p][2]-1
        room[a] = room[a] + z[p][3]
        if room[a] < 0 or room[a] > 9:
            print("Error")
            exit()

def reset_list():
    z.clear()
    for q in range(10):
        room[q] = 0


while i < n:
    x = map(int,input().split())
    x = list(x)
    y.append(x)
    i += 1

y.sort()

for i in range(4):
    for k in range(3):
        calculate(room_list(i,k))
        R = [str(j) for j in room]
        R = " ".join(R)
        print("",R)
        reset_list()
    if i < 3:
        print("#"*20)
