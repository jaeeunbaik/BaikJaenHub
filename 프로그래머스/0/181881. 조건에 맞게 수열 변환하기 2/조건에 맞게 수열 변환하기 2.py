def solution(arr):
    x=0
    result=[]
    result.append(tuple(arr))
    while True:
        for idx in range(len(arr)):
            if arr[idx]>=50 and arr[idx]%2==0:
                arr[idx]=int(arr[idx]/2)
            elif arr[idx]<50 and arr[idx]%2==1:
                arr[idx]=arr[idx]*2+1
        result.append(tuple(arr))
        x+=1
        if result[x]==result[x-1]:
            break
    return x-1