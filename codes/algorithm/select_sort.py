def select_sort(target):
    for i in range(len(target)-1):
        min_idx = i
        for j in range(i, len(target)):
            if target[j] < target[min_idx]: # 부등호 반대하면 내림차순
                min_idx = j
        target[i], target[min_idx] = target[min_idx], target[i]
    return target

print(select_sort([5,2,3,4,1]))
        
