import sys

#sys.stdin = open("input.txt", "r")
n, m = map(int, sys.stdin.readline().split())
strings = {sys.stdin.readline().rstrip() for _ in range(n)}
count = 0

for _ in range(m):
    word = sys.stdin.readline().rstrip()
    if word in strings:
        count += 1

print(count)