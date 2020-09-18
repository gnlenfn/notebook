def solution(board, moves):
    answer = 0
    stack = []
    for col in moves:
        for row in range(len(board[col-1])):
            if board[row][col-1] != 0:
                target = board[row][col-1]
                board[row][col-1] = 0
                if stack and stack[-1] == target:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(target)
                break
            
    return answer