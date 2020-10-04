import sys

a, b = sys.stdin.readline().split()
s_a, s_b = int(a[::-1]), int(b[::-1])

print(max(s_a, s_b))
