from collections import deque
def solution(x, y, box):
    answer = 0
    queue = deque()
    non_checked = x * y
    visited = [[False] * x for _ in range(y)]
    
    for row in range(y):
        for col in range(x):
            if box[row][col] == 1:
                queue.append([row, col, 0])
                non_checked -= 1
                visited[row][col] = True
            elif box[row][col] == -1:
                non_checked -= 1
                visited[row][col] = True

    while queue:
        row, col, day = queue.popleft()
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            new_row, new_col = row + dy, col + dx
            if 0 <= new_row < y and 0 <= new_col < x and not visited[new_row][new_col]:
                queue.append((new_row, new_col, day+1))
                visited[new_row][new_col] = True
                non_checked -= 1
                answer = day + 1

    return answer if non_checked == 0 else -1

if __name__ == "__main__":
    x, y = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(y)]
    print(solution(x, y, box))