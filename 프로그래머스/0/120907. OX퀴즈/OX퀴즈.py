def solution(quiz):
    answer = []
    for q in quiz:
        [X, op, Y, eq, Z] = q.split(' ')
        if eval(''.join([X, op, Y])) == int(Z):
            answer.append("O")
        else: answer.append("X")
    return answer