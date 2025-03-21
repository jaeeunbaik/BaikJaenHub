# 일단 k 개를 지워야 하니까, 끝에서 k개만 빼고 그 중에서 제일 큰 숫자를 찾아.
# 걔가 맨 첫번째 숫자가 되는거야. 그리고 그 이후로, 그 다음으로 큰 숫자를 찾아. 이제 범위가 하나 늘었어.
# 그 다음으로 !
def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)