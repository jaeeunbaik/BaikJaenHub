def solution(citations):
    h_index = 0
    citations = sorted(citations, reverse=True)
    for i, c in enumerate(citations):
        if c >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index