def solution(my_string, m, c):
    answer = ''
    c_col = []
    for n in range(len(my_string)//m):
        c_col.append(my_string[n*m:(n+1)*m+1][c-1])
    return ''.join(c_col)