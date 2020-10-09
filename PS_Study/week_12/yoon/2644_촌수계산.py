# DFS
from collections import defaultdict
from collections import deque
import sys

def find_relations(target1, target2, family):
    step = 0
    queue, visited = deque(), set()
    queue.append(target1)
    visited.add(target1)
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current == target2:
                return step

            for direct in family[current]:
                if direct not in visited:
                    queue.append(direct)
                    visited.add(direct)
        step += 1
    
    return -1

sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline().rstrip())
target1, target2 = map(int, sys.stdin.readline().split())
edges = int(sys.stdin.readline().rstrip())

family = defaultdict(set)

for _ in range(edges):
    parent, child = map(int, input().split())
    family[parent].add(child)
    family[child].add(parent)

print(find_relations(target1, target2, family))