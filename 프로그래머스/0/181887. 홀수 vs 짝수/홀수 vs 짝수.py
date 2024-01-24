def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    idx = 1
    for num in num_list:
        if idx&1==1:
            odd += num
        elif idx&1==0:
            even += num
        idx+=1
    if odd>even: answer=odd
    elif odd<even: answer=even
    else: answer = odd
    return answer