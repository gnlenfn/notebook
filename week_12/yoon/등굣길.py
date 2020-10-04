def solution(m, n, puddles):
    answer = 0
    route = [[0] * (m+1) for _ in range(n+1)]
    route[1][1] = 1
    for row in range(1, n+1):
        for col in range(1, m+1):
            if row == col == 1:
                continue
            if [col, row] not in puddles:
                if route[row-1][col] in puddles and route[row][col-1] not in puddles:
                    route[row][col] = route[row][col-1]

                elif route[row][col-1] in puddles and route[row-1][col] not in puddles:
                    route[row][col] = route[row-1][col]

                else:
                    route[row][col] = route[row-1][col] + route[row][col-1]

                
    return route[n][m] % 1_000_000_007

print(solution(4, 3, [[2,2]]))