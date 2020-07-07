def solution(x):
    if x == n:
        return 1
    if x > n:
        return 0
    return solution(x+10) + 2 * solution(x+20)


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print('#%d %s'%(test_case, solution(0)))