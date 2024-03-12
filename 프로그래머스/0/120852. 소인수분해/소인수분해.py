def solution(n):
    answer = []
    for i in range(1, n+1):
        div = []
        for x in range(1, i//2+1): #소수인지
            if i%x==0:
                div.append(x)
        if len(div)==1 and n%i==0: #소수라면, 나누어 떨어지면 소인수!
            answer.append(i)
    return answer