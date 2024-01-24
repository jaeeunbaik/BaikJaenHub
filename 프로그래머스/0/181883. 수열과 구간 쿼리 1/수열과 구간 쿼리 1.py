def solution(arr, queries):
    for s, e in queries:
        for idx in range(len(arr)):
            if idx>=s and idx<=e:
                arr[idx]+=1
    return arr