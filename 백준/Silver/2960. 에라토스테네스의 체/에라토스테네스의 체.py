N , K = list(map(int, input().split(' ')))
    
#7, 3
prime = [True] * (N+1)
k = 0
for i in range(2, N+1):
    if prime[i]:
        for j in range(i, N+1, i):
            if prime[j]:
                prime[j] = False
                k += 1
                if int(k) == int(K):
                    print(j)
                    break