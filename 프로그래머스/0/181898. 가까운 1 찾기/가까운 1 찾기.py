def solution(arr, idx):
    answer = -1
    while answer == -1 and idx < len(arr):
        if arr[idx] == 1:
            answer = idx
        else: idx += 1
    return answer