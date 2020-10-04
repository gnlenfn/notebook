import sys

"""
30의 배수 판별법:
1. 각 자릿수의 합의 3의 배수
2. 일의 자리가 0
두 조건을 모두 만족하면 30의 배수가 된다.
주어진 숫자로 만들 수 있는 가장 큰 30의 배수는 
위의 두 조건을 만족하면서, 내림차순으로 정렬한 것
"""

def solution(n):
    Nlist = list(n)
    if '0' not in Nlist:
        return -1
    check = [int(x) for x in Nlist]
    if sum(check) % 3 != 0:
        return -1
    answer = ''.join(sorted(Nlist, reverse=True))
    return answer

if __name__ == "__main__":
    n = sys.stdin.readline().strip()
    a = solution(n)
    print(a)