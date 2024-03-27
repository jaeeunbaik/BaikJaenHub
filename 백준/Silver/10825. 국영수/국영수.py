N = int(input())

scores = []

for n in range(N):
    scores.append(''.join(input()).split(' '))

scores.sort(key = lambda x: ((-1)*int(x[1]), int(x[2]), (-1)*int(x[3]), x[0]))

for score in scores:
    print(score[0])