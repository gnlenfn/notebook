triangle = []
n = int(input())
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for idx in range(n-2, -1, -1):
    for j in range(len(triangle[idx])):
        triangle[idx][j] = max(triangle[idx][j]+triangle[idx+1][j], triangle[idx][j]+triangle[idx+1][j+1])

print(triangle[0][0])