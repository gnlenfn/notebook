from collections import defaultdict
def solution(N, stages):
    result = defaultdict(int)
    complete = [0 for _ in range(N+2)]
    for stage in stages:
        complete[stage] += 1
    
    total = len(stages)
    for stage in range(1, N+1):
        total -= complete[stage-1]
        if total == 0:
            result[stage]
        else:
            result[stage] = complete[stage] / total
    
    return sorted(result, key=lambda x : result[x], reverse=True)