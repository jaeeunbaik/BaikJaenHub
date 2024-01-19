def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    for [s,e] in queries:
        my_string[s:e+1] = reversed(my_string[s:e+1])
    my_string = map(str, my_string)
    return ''.join(my_string)