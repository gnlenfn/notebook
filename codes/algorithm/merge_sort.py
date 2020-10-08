def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while left or right:
        if left and right:
            if left[0] > right[0]:
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]
        elif not left:
            result.append(right[0])
            right = right[1:]
        elif not right:
            result.append(left[0])
            left = left[1:]

    return result

print(merge_sort([3,1,4,2,0]))

