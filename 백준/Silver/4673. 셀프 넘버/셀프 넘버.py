def d(num):
    digit = list(map(int, str(num)))
    self_num = num + sum(digit)
    return self_num

self_num = [True]*10001


for i in range(1,10001):
    if d(i) < 10001:
        if self_num[d(i)] == True:
            self_num[d(i)] = False

for i in range(1, 10001):
    if self_num[i] == True:
        print(i) 