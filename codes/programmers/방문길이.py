def solution(dirs):
    move = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    point = (0, 0)
    passed = set()
    
    for dir in dirs:
        x, y = point
        dx, dy = move[dir]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            passed.add((x, y, nx, ny))
            passed.add((nx, ny, x, y))
            point = (nx, ny)
    return len(passed) // 2

print(solution("LRLRLR"))