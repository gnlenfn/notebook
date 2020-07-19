def dfs(stack):
    global result
    if start == goal:
        return
    while stack:
        tmp = stack.pop()
        visit[tmp] = 1
        for i in matrix[tmp]:
            if i == goal:
                result += 1
            if visit[i] == 1:
                continue
            else:
                
                visit[i] = 1
                stack.append(i)
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    matrix  = [[] for _ in range(V+1)]       # 그래프 그리가 (1D)
    visit = [0] * (V + 1)                    # 방문한 노드

    for _ in range(E):
        x, y = map(int, input().split())
        matrix[x].append(y)

    visit = [0] * (V + 1) 
    start, goal = map(int, input().split())
    result = 0
    stack = [start]
    dfs(stack)

    print(f'#{test_case} {result}')