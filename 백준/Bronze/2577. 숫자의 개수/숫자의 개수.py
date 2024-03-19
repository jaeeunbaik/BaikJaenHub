num = [0]*3
for i in range(3):
    num[i] = int(input())

result = list(map(int, str(num[0] * num[1] * num[2])))

times = [0] * 10

for i in range(len(result)):
    times[result[i]] += 1

for i in range(0, 10):
    print(times[i])