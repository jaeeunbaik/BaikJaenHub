def solution(nums):
    N = len(nums)
    num_types = len(set(nums))
    if num_types >= N // 2:
        return N // 2
    else: return num_types