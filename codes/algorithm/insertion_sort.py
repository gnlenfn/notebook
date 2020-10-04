def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key: # 부등호 반대하면 내림차순
            arr[i+1] = arr[i]
            i -= 1
            print(arr)
        arr[i+1] = key
    return arr

d = [4,1,2,3,6,5]
print(insertion_sort(d))