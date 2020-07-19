def bfs(queue):
   # global num
    if start == goal:
        return
    num = 0
    while queue:
        num += 1    # 간선 1개 이동
        len_q = len(queue)

        for _ in range(len_q):
            tmp = queue.pop(0)
            for i in matrix[tmp]:
                if visited[i] == 1:
                    continue
                else:
                    visited[i] = 1
                    queue.append(i)
        if goal in queue:
            return num


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
                                         # queue = [  ]
    matrix  = [[] for _ in range(V+1)]   # [[] [3, 4] [3, 5] [] [6] [] []]
    visited = [0] * (V+1)                # [0      0 0 1 0 0 0]


    # 그래프 생성
    for _ in range(E):
        x, y = map(int, input().split())
        matrix[x].append(y)
        matrix[y].append(x)
    start, goal = map(int, input().split())
    
    visited[start] = 1 # start node visited
    queue = [start]    # queue.append(start)
    #num = 0            # number of edges
    res = bfs(queue)

    print(f'#{test_case} {res}')
