def solution(my_string, num1, num2):
    my_string = list(my_string)
    tmp = my_string[num2]
    my_string[num2] = my_string[num1]
    my_string[num1] = tmp
    return ''.join(my_string)