import math

def solution(arr):
    tmp = math.log2(len(arr))
    if tmp % 1==0:
        pass
    else: tmp = (tmp)//1+1
    
    while len(arr)<2**tmp:
        arr.append(0)
    return arr