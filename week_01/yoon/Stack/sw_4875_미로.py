def confirm(x, y):                                      # 좌표 (x, y)에 방문 가능한지 확인
    return 0 <= x < row and 0 <= y < row and (maze[x][y] == 0 or maze[x][y] == 3)

def dfs(x, y):
    global result
    if maze[x][y] == 3:                                 # 좌표 값이 3이면 값 반환
        result = 1
        return 

    stack.append((x, y))
    for i in range(4):                                  # 이동방향 -- 아래 참조
        nx, ny = x + dx[i], y + dy[i]
        if confirm(nx, ny) and (nx, ny) not in stack:   # x, y가 0보다 크거나 같고 row보다 작아야함 (미로 내의 좌표)
            dfs(nx, ny)                                 # 새로운 좌표 (nx, ny)에 방문한 적이 없어야함


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
    stack = []
    result = 0
    dfs(start_x, start_y)                             # global result 말고는 다른 방법 없었나?
    print(f'#{test_case} {result}')






