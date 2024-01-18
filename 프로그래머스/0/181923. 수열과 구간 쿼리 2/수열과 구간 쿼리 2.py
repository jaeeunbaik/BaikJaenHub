def solution(arr, queries):
    answer = [0]*len(queries[:])
    for n in range(len(queries[:])):
        [s,e,k] = queries[n][:]
        
        arr_set = set(arr[s:e+1])
        if max(arr_set)>k:
            while min(arr_set)<=k:
                arr_set.remove(min(arr_set))
            answer[n] = min(arr_set)
        else: answer[n] = -1
    return answer