
N = int(input())

def curious(num):
    digit = list(map(int, str(num)))
    if sum(digit) != 0:
        if num % sum(digit) == 0:
            return True

numbers = [False]*(N+1)
answer = 0

for i in range(1,N+1):
    if curious(i):
        numbers[i] = True
for i in range(1,N+1):
    if curious(i):
        answer += 1

print(answer)
