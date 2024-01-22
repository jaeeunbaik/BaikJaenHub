def solution(my_string, is_prefix):
    answer = 0
    prefices = []
    for i in range(len(my_string)):
        prefices.append(my_string[:i])
    if is_prefix in prefices:
        answer = 1
    else: answer = 0
    return answer