def solution(n):
    return div(n)

def div(num):
    div = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            div.append(i)
            if num // i != i:
                div.append(num // i)
    return sorted(div)