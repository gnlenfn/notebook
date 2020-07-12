def confirm(x, y):                                                  # 좌표 (x, y)에 방문 가능한지 확인
    return 0 <= x < row and 0 <= y < row and (maze[x][y] == 0 or maze[x][y] == 3)

def bfs(x, y):
    global result
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        start_x, start_y = queue.pop(0)
        for i in range(4):                                          # 이동방향 -- 아래 참조
            nx, ny = start_x + dx[i], start_y + dy[i]
            if confirm(nx, ny) and visited[nx][ny] == 0:            # x, y가 0보다 크거나 같고 row보다 작아야함 (미로 내의 좌표)
                queue.append((nx, ny))                              # 새로운 좌표 (nx, ny)에 방문한 적이 없어야함
                visited[nx][ny] = 1
                distance[nx][ny] = distance[start_x][start_y] + 1
                if maze[nx][ny] == 3:                              
                    result = distance[nx][ny] - 1
                    return

T = int(input())
for test_case in range(1, T+1):
    row = int(input())
    maze = []
    for r in range(row):
        line = list(map(int,input()))
        a = []
        for s in range(len(line)):
            a.append(line[s])
            if line[s] == 2:
                start = (r, s)
        maze.append(a)

    start_x, start_y = start
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    '''
    dx[0] dy[0] --> right
    dx[1] dy[1] --> left
    dx[2] dy[2] --> down
    dx[3] dy[3] --> up
    '''
    distance = [[0] * row for _ in range(row)]                      # 출발 좌표에서 각 좌표까지의 거리 입력할 곳
    visited = [[0] * row for _ in range(row)]                       # 방문했던 좌표 기록하기 위한
    queue = []                                                      # bfs 위한 queue
    result = 0
    bfs(start_x, start_y)                         
    print(f'#{test_case} {result}')
