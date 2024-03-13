T = int(input())

ckh = []
bsh = []

for _ in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = list(map(int, input().split(' ')))
    ckh.append([x_1, y_1, r_1])
    bsh.append([x_2, y_2, r_2])

for t in range(T):
    a_1 = ckh[t][0]
    a_2 = bsh[t][0]
    b_1 = ckh[t][1]
    b_2 = bsh[t][1]
    r_1 = ckh[t][2]
    r_2 = bsh[t][2]
    d = ((a_1-a_2)**2+(b_1-b_2)**2)**0.5 # 중심사이의 거리

    if a_1==a_2 and b_1==b_2 and r_1==r_2:
        print(-1)
    elif d > r_1 + r_2 or d < abs(r_1 - r_2):
        print(0)
    elif d == r_1 + r_2 or d == abs(r_1 - r_2):
        print(1)
    elif d > abs(r_1 - r_2) and d < r_1 + r_2:
        print(2)