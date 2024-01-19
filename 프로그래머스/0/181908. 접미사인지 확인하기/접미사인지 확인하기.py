def solution(my_string, is_suffix):
    answer = 0
    suffix = []
    for i in range(len(my_string)):
        suffix.append(my_string[i:len(my_string)])
                      
    if is_suffix in suffix:
            answer = 1
    else: 
            answer = 0
                      
    return answer