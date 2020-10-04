def check_next(next_row, next_col, n, snail):
    return next_row < 0 or next_row >= n or next_col > next_row or snail[next_row][next_col]
    # next가 없는 경우를 return --> 방향을 바꾸는 지점 찾는 것
    
def move_next(cur_row, cur_col, dir):
    DELTA = {"U": (-1, -1), "D": (1, 0), "R": (0, 1)}
    next_row, next_col = cur_row + DELTA[dir][0], cur_col + DELTA[dir][1]
    return next_row, next_col
    
def solution(n):
    NEXT = {"D": "R", "R": "U", "U": "D"}
    snail = [[0] * i for i in range(1, n+1)]
    N = sum(range(1, n+1))
    
    cur_row, cur_col, dir = 0, 0, "D"
    for idx in range(1, N+1):
        snail[cur_row][cur_col] = idx
        if check_next(*move_next(cur_row, cur_col, dir), n, snail):
            dir = NEXT[dir]
        cur_row, cur_col = move_next(cur_row, cur_col, dir)

    answer = sum(snail, [])
    return answer