apart1 = [[0] * 10, [0] * 10, [0] * 10]
apart2 = [[0] * 10, [0] * 10, [0] * 10]
apart3 = [[0] * 10, [0] * 10, [0] * 10]
apart4 = [[0] * 10, [0] * 10, [0] * 10]
log = []
log_a1 = []
log_a2 = []
log_a3 = []
log_a4 = []


def print_room(x):
    apart = x
    for i in range(3):
        R = [str(j) for j in apart[i]]
        R = " ".join(R)
        print("",R)


def print_hash():
    print("#" * 20)


def caluculate(x):
    apart = [[0] * 10, [0] * 10, [0] * 10]
    for i in x:
        if i[1] == 1:
            apart[0][i[2] - 1] = apart[0][i[2] - 1] + i[3]
        if i[1] == 2:
            apart[1][i[2] - 1] = apart[1][i[2] - 1] + i[3]
        if i[1] == 3:
            apart[2][i[2] - 1] = apart[2][i[2] - 1] + i[3]
    
    return apart


N = int(input())
for i in range(N):
    x = list(map(int, input().split()))
    log.append(x)

for i in log:
    if i[0] == 1:
        log_a1.append(i)
    elif i[0] == 2:
        log_a2.append(i)
    elif i[0] == 3:
        log_a3.append(i)
    else:
        log_a4.append(i)

print(log_a1)
print(log_a2)
print(log_a3)
print(log_a4)

"""
apart1 = caluculate(log_a1)
apart2 = caluculate(log_a2)
apart3 = caluculate(log_a3)
apart4 = caluculate(log_a4)
"""
