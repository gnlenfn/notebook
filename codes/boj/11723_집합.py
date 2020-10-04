import sys
tc = int(sys.stdin.readline())

S = set()
for _ in range(tc):
    command = sys.stdin.readline().strip().split()
    if len(command) > 1:
        num = int(command[1])
    if command[0] == "add":
        S.add(num)
    elif command[0] == "remove" and num in S:
        S.remove(num)
    elif command[0] == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif command[0] == "all":
        S = set(range(1, 21))
    elif command[0] == "empty":
        S.clear()