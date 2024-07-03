def solution(n):
    if n == 1:
        return [[1]]
    
    answer = [[0]*n for i in range(n)]
    mode = 'r'
    i = 0
    j = 0
    
    for k in range(n*n):
        answer[i][j] = k+1
        if mode == 'r':
            j += 1
            if j == n-1 or answer[i][j+1] != 0:
                mode = 'd'
        elif mode == 'l':
            j -= 1
            if j == 0 or answer[i][j-1] != 0:
                mode = 'u'
        elif mode == 'u':
            i -= 1
            if answer[i-1][j] != 0:
                mode = 'r'
        elif mode == 'd':
            i += 1
            if i == n-1 or answer[i+1][j] != 0:
                mode = 'l'
    return answer