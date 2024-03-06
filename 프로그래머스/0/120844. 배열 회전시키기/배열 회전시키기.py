def solution(numbers, direction):
    answer = [0]*len(numbers)
    if direction == "right":
        answer[1:] = numbers[:-1]
        answer[0] = numbers[-1]
    else:
        answer[:-1] = numbers[1:]
        answer[-1] = numbers[0]
    return answer