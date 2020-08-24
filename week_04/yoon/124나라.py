def solution(n):
    answer = ''
    while n:
        n, nam = divmod(n, 3) # n, nam = n //3 , n % 3
        answer = "412"[nam] + answer
        if nam == 0:
            n -= 1
    return answer


print(solution(6))
#print(solution(9))
#print(solution(11))