def solution(n):
    answer = []
    for i in range(n): #행단위
        row = []
        for j in range(n): #열단위
            if i == j:
                row.append(1)
            else: row.append(0)
        answer.append(row)
    return answer