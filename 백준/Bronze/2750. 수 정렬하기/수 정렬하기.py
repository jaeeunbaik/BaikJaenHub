N = int(input())

num = []
for n in range(N):
    num.append(int(input()))
num.sort()
for n in range(N):
    print(num[n])