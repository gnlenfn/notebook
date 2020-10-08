def solution(n, times):
    answer = 0
    left, right = 1, n * max(times)
    while left <= right:
        mid = (left + right) // 2
        affordable = sum([mid // t for t in times])
        
        if n > affordable:
            left = mid + 1
        else:
            if n <= affordable:
                answer = mid
            right = mid - 1
    return answer