def operator(idx, numbers, target):
    global answer
    if idx < len(numbers):
        numbers[idx] *= 1
        operator(idx + 1, numbers, target)

        numbers[idx] *= -1
        operator(idx + 1, numbers, target)
    
    elif sum(numbers) == target:
        answer += 1
        return 

def solution(numbers, target):
    global answer
    answer = 0

    operator(0, numbers, target)
    return answer

print(solution([1,1,1,1,1], 3))