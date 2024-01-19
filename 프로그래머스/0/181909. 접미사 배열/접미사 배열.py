def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(''.join(my_string[i:len(my_string)]))
    answer.sort()
    return answer