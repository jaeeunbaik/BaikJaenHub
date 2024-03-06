def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        tmp = num_list[i*n:i*n+n]
        answer.append(tmp)
    return answer