def solution(arr):
    for idx, ele in enumerate(arr):
        if ele>= 50 and ele%2==0:
            arr[idx] = arr[idx]/2
        elif ele<50 and ele%2==1:
            arr[idx] = arr[idx]*2
    return arr