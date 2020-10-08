def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    while A:
        if A[-1] < B[-1]:
            A.pop()
            B.pop()
            answer += 1
        else:
            A.pop()
    return answer