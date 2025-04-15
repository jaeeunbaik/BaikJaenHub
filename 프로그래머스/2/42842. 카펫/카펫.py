def solution(brown, yellow):
    answer = []
    total = brown + yellow
    if total ** 0.5 % 1 == 0:
        a = int(total ** 0.5)
        return [a, a]
    for b in range(3, int(total ** 0.5) + 1):  # 가로: a, 세로: b
        a = total // b
        if a * b == total and a * 2 < brown and b * 2 < brown and a * 2 + (b-2) * 2 == brown:
            return [a, b]
        
