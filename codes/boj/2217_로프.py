n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope = sorted(rope, reverse=True)
answer = []
for idx in range(len(rope)):
    answer.append(rope[idx] * (idx+1))

print(max(answer))