def solution(l, r):
    answer = []
    num_list = range(l,r+1)
    for i in num_list:
        if all(k in ['0', '5'] for k in str(i)):
            answer.append(i)
    if answer == []:
        answer = [-1]
    return answer