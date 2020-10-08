def solution(priorities, location):
    p = [(idx, val) for idx, val in enumerate(priorities)]
    queue = []
    
    while p:
        cur = p.pop(0)
        curIdx = cur[0]
        curVal = cur[1]
        valList = [val for idx, val in p]
        
        if valList:
            maxVal = max(valList)
        if curVal >= maxVal:
            queue.append(cur)
        else:
            p.append(cur)
    
    for idx, val in enumerate(queue):
        if val[0] == location:
            return idx + 1
