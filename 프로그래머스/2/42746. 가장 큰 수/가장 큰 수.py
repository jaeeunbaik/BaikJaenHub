def solution(numbers):
    answer = ''
    # 이어 붙이기
    # 1. numbers에 숫자 하나씩 접근, 정답이 너무 클 걸 방지해서 문자열로 바꾸라는데 굳이 숫자로 저장해야할 이유 ..
    # 2. 젤 큰 자리수의 숫자끼리만 비교해서 정렬하고 그 순서대로 붙이기, 그 다음 자리수 정렬? 3 vs 30? 
    #    - 젤 큰 자리수부터 숫자끼리 비교 & 0이 젤 꼴지 그 바로 앞이 아무것도 없는 거 . .
    numbers = sorted(numbers, key=lambda x: str(x)*3, reverse=True)
    numbers = list(map(str, numbers))
    return str(int(''.join(numbers)))