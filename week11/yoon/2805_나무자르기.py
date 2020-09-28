import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

trees.sort() # 이분탐색은 정렬된 상태에서만!
left, right = 0, trees[-1]
answer = 0
while left <= right:
    cut = 0
    mid = (left + right) // 2
    for length in trees:
        cut += max((length - mid), 0)
    
    if cut < m:
        right = mid - 1
    else:
        answer = mid
        left = mid  + 1

print(answer)