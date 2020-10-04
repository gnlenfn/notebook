n, row, col = map(int, input().split())

num = 0
while n > 0:
    mid = (2 ** n) // 2
    if n > 1:
        if mid > row and mid <= col: # 2사분면
            num += mid ** 2
            col -= mid
    
        elif mid <= row and mid > col: # 3사분면
            num += (mid ** 2) * 2
            row -= mid
    
        elif mid <= row and mid <= col: # 4사분면
            num += (mid ** 2) * 3
            row -= mid
            col -= mid
    else:
        if row == 0 and col == 1:
            num += 1
        elif row == 1 and col == 0:
            num += 2
        elif row == 1 and col == 1:
            num += 3
    n -= 1
print(num)