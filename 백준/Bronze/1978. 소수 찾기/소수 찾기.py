def is_prime(num):
    if num == 1:
        return False
    
    for n in range(2, int(num**0.5+1)):
        if num % n == 0:
            return False
    return True
    
num = []
N_number = int(input())
N = list(map(int, input().split(' ')))
for n in N:
    if is_prime(n):
        num.append(n)
    else: pass
    
print(len(num))