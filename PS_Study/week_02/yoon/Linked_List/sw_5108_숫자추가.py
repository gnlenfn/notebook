T = int(input())

for test_case in range(1, T+1):
    n, m, l = map(int, input().split())

    target = list(map(int, input().split()))
    for _ in range(m):
        idx, item = map(int, input().split())
        target.insert(idx, item)
    print(f'#{test_case} {target[l]}')