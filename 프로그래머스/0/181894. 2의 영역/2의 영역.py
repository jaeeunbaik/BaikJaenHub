def solution(arr):
    answer = []
    for idx in range(len(arr)):
        if arr[idx]==2:
            answer.append(idx)
    if answer == []:
        return [-1]
    return arr[answer[0]:answer[len(answer)-1]+1]