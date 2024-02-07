def lcd(num1, num2):
    x = max(num1, num2)
    y = min(num1, num2)
    while y!=0:
        x, y = y, x%y
    lcd = num1*num2//x
    return lcd


def solution(n):
    return lcd(n, 6)//6