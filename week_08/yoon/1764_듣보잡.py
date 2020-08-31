import sys
n, m = map(int, sys.stdin.readline().split())

team_n = set()
team_m = set()
for _ in range(n):
    name = sys.stdin.readline().strip()
    team_n.add(name)

for _ in range(m):
    name = sys.stdin.readline().strip()
    team_m.add(name)

result = sorted(team_n & team_m)
print(len(result))
for name in result:
    print(name)