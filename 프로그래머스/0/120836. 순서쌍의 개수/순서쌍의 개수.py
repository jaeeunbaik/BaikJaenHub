import math
def solution(n):
    answer = 0
    for i in range(int(math.sqrt(n))):
        if n%(i+1)==0:
            answer+=1
    if math.sqrt(n)%1==0:
        answer = 2*answer - 1
    else: answer = 2*answer
    return answer