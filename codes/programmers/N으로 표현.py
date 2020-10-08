from collections import defaultdict
def solution(N, number):
    MAX_RANGE = 8
    dp = [set() for _ in range(MAX_RANGE+1)]

    for i in range(1, MAX_RANGE+1):
        for j in range(1, i):
            dp[i] |= calculate(dp[j], dp[i-j]) # 사칙연산 결과 합집합
        dp[i].add(int(str(N) * i))             # 이어 붙이기
        if number in dp[i]:
            return i
    return -1

def calculate(numbers1, numbers2):
    result = set()
    for num1 in numbers1:
        for num2 in numbers2:
            result.add(num1 + num2)
            result.add(num1 - num2)
            result.add(num1 * num2)
            if num2 != 0:
                result.add(num1 // num2)
    return result

print(solution(5, 12))