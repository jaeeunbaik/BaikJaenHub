N, M = list(map(int, input().split(' ')))

basket = [0] * (N+1)

for n in range(N+1):
    basket[n] = n
    
tmp = 0
for _ in range(M):
    s1, s2 = list(map(int, input().split(' ')))
    tmp = basket[s2]
    basket[s2] = basket[s1]
    basket[s1] = tmp
answer = ''
for n in range(1, N+1):
    answer += str(basket[n]) + ' '
print(answer)