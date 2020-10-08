def insert(idx, last):              # last: target number / idx: currend index
    global count
    if idx <= last:
        insert(idx * 2, last)       # left: (current idx) * 2
        tree[idx] = count
        count += 1
        insert(idx * 2 + 1, last)   # right: (current idx) * 2 + 1

T = int(input())
for tesc_case in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    count = 1
    insert(1, n)

    print(f"#{tesc_case} {tree[1]} {tree[n//2]}") # root node idx = 1 

