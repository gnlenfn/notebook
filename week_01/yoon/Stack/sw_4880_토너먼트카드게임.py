def rsp(x, y):
    if group[x] == group[y]:
        return [min(x, y)]
    elif abs(group[x]-group[y]) == 1:
        return [x] if group[x]>group[y] else [y]
    elif abs(group[x]-group[y]) == 2:
        return [x] if group[x]<group[y] else [y]

def divide(nums):
    if len(nums) == 1:
        return nums

    pivot = (len(nums) + 1) // 2 
    left = nums[:pivot]
    right = nums[pivot:]

    left = divide(left)
    right = divide(right)
    return rsp(left[0], right[0])

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    group = list(map(int, input().split()))
    nums = list(range(n))

    answer = divide(nums)
    print(f'#{test_case} {answer[0] + 1}')
    
