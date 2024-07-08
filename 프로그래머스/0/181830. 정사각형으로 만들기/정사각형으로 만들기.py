def solution(arr):
    col = len(arr[0])
    row = len(arr)
    if row == col:
        return arr
    elif row > col:
        for r in range(row):
            arr[r].extend([0]* (row-col))
    elif row < col:
        for i in range(col - row):
            arr.append([0]*col)
    return arr