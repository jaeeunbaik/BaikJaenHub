# def calculate(tmp, cnt, N, memo, number, sym):
#     if cnt > 8:
#         return None
#     tmp = int(eval(str(tmp) + sym + str(N)))  # 입력값으로 새로운 사칙 연산 계산
#     if tmp == number:
#         memo[cnt] = True
#     for s in ["+", "-", "*", "/"]:
#         calculate(tmp, cnt + 1, N, memo, number, s)
#         if N < 10:
#             calculate(tmp, cnt + 2, 10*N + N, memo, number, s)

# def solution(N, number):
#     answer = 0
#     memo = [False] * 9
#     cnt = 0
#     calculate(0, 1, N, memo, number, "+")
#     calculate(0, 2, 10*N + N, memo, number, "+")
#     print(memo)
#     for i in range(9):
#         if memo[i]:
#             return i
#     return -1  # 이 방식으로 하면 555로 된 연산은 못함..

def solution(N, number):
    if N == number:
        return 1
    answer = -1
    # N으로만 구성된 숫자 배열, N 사용 횟수에 따른 가능한 결과값 초기 구성
    arr = [set([int(str(N)*(i+1))]) for i in range(9)]
    # print(arr)
    # arr에 있는 값들이 서로서로 연산자가 되어서 arr에 값을 추가하고(N사용횟수별 가능한 숫자), 그 값에 number가 있으면 answer 출력
    for i in range(1,8):  # arr 의 1부터 업데이트 함. 
        for j in range(i):  # N 횟수 사용 합이 총 i여야 함, i 보다 작은 j
            for op1 in arr[j]:  # i보다 작은 j 횟수에 대해서 가능한 숫자들
                for op2 in arr[i-j-1]:  # i만큼 N사용했고, 총 j사용해야하니까 arr[i-j-1]에서 가능한 숫자들 가져오기.
                    arr[i].add(op1+op2)
                    arr[i].add(op1-op2)
                    arr[i].add(op1*op2)
                    if not op2==0:
                        arr[i].add(op1/op2)
        if number in arr[i]:
            answer = i+1
            break
    return answer