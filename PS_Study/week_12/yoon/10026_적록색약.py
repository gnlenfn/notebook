import sys
from collections import deque

def bfs(row, col, image, visited, n):
    queue = deque()
    queue.append((row, col))
    color = image[row][col]
    
    while queue:
        row, col = queue.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            new_row, new_col = row + dy, col + dx

            if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col] and image[new_row][new_col] == color:
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
    return 1


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")

    n = int(sys.stdin.readline().rstrip())
    image = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    image_RG = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if image[y][x] == "G":
                image_RG[y][x] = "R"
            else:
                image_RG[y][x] = image[y][x]

    visited = [[False] * n for _ in range(n)]
    visited_RG = [[False] * n for _ in range(n)]
    answer = 0
    answer_RG = 0
    for row in range(n):
        for col in range(n):
            if not visited[row][col]:                
                answer += bfs(row, col, image, visited, n)
            if not visited_RG[row][col]:
                answer_RG += bfs(row, col, image_RG, visited_RG, n)
                
    print(answer, answer_RG)