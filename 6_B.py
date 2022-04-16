mark_list = ["S","H","D","C"]
num_list = list(range(1,14))
num_list = [str(i) for i in num_list]
char_list = []
answer = []

def brute(x):   #総当たりでリスト内に入力したものが含まれるのかを検索
    for j in range(0,13):
        if [mark_list[x],num_list[j]] not in char_list:
            answer.append([mark_list[x],num_list[j]])
    return answer



n = int(input())
count = 0

while count < n:
    x = list(input().split())
    char_list.append(x)
    count += 1

for k in range(len(mark_list)):
    if k == 0:
        brute(k)
    elif k == 1:
        brute(1)
    elif k == 2:
        brute(2)
    else:
        brute(3)

for l in range(len(answer)):
    print(answer[l][0],answer[l][1])



