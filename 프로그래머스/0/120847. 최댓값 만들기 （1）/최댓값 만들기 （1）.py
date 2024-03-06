def solution(numbers):
    s_numbers = sorted(numbers)
    return s_numbers[-1]*s_numbers[-2]