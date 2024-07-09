from collections import deque
def solution(numbers):
    answer = []
    nums = deque(numbers)
    while nums:
        num = nums.popleft()
        for n in nums:
            answer.append(num * n)
    return max(answer)