def solution(n):
    answer = 0
    for num in range(1,n+1):
        divisor = []
        for i in range(1,num//2+1):
            if num%i==0:
                divisor.append(i)
        if len(divisor) >= 2:
            answer+=1
    return answer