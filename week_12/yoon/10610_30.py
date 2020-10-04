import sys

def find(target):
    if "0" not in target or sum(map(int, target)) % 3:
        return -1
    return "".join(sorted(list(target), reverse=True))      

if __name__ == "__main__":
    target = sys.stdin.readline().rstrip()
    print(find(list(target)))
