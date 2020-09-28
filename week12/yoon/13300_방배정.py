import sys
from collections import defaultdict

#sys.stdin = open("input.txt", 'r')
students, capacity = map(int, sys.stdin.readline().split())
guys = defaultdict(int)
rooms = 0

for _ in range(students):
    gender, grade = sys.stdin.readline().split()
    guys[gender+grade] += 1

for child in guys:
    need, left = divmod(guys[child], capacity)
    rooms += need

    if left:
        rooms += 1

print(rooms)