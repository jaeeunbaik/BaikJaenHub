def solution(numbers):
    primes = set()
    # 1번) **만들 수 있는 모든 숫자를 만들기** <- dfs
    numbers = list(map(int, numbers))
    numbers.sort()
    result = set()
    used = [False] * len(numbers)
    dfs([], used, numbers, result)
    result = [list(r) for r in result]
    for r in result:
        num = ''
        for i in r:
            num += str(i)
        if is_prime(num):
            primes.add(int(num))
    return len(primes)

def dfs(path, used, numbers, result):
    if path:  # 빈 path 제외하고 저장, []에 숫자가 하나씩 추가됐으니까 path는 list.
        result.add(tuple(path))  # set을 사용해 중복 제거 , result 가 해당 자리수에 해당하는 가능한 모든 숫자 조합 ~?

    for i in range(len(numbers)):
        if used[i]:
            continue
        # 중복 숫자 방지: 이전 값과 동일하고, 그 이전 값이 아직 사용되지 않았으면(중복경로가 생성된다면) skip
        if i > 0 and numbers[i] == numbers[i-1] and not used[i-1]:
            continue
        used[i] = True
        path.append(numbers[i])
        dfs(path, used, numbers, result)
        path.pop()
        used[i] = False

def is_prime(num):
    if int(num) == 1:
        return False
    if int(num) in [2, 3, 5, 7]:
        return True
    if int(num[-1]) % 2 == 0 or int(num[-1]) == 5:
        return False
    for n in range(2, int(int(num) ** 1/2)):
        if int(num) % n == 0:
            return False
    return True