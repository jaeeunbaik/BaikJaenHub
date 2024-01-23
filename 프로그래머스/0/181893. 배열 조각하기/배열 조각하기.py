def solution(arr, query):
    for q in range(len(query)):
        if q&1==0:
            arr = arr[0:query[q]+1]
        else: arr = arr[query[q]:]
    return arr