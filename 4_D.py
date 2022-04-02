A = int(input()) # 計算中に使えてない
B = input()
B1 = B.split()

list = [int(i) for i in B1]

print(min(list), max(list), sum(list))