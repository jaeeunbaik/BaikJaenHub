def solution(balls, share): #5C2
    answer = 0
    b_fac = fac(balls)
    s_fac1 = fac(share)
    s_fac2 = fac(balls-share)
    answer = b_fac // (s_fac1*s_fac2) 
    return answer

def fac(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer