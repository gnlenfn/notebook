from collections import defaultdict
def solution(gems):
    answer = [0, len(gems)]
    gem_kinds = len(set(gems))
    left, right = 0, 0
    bought = defaultdict(int)
    bought[gems[0]] = 1
    
    while left < len(gems) and right < len(gems):
        if len(bought) == gem_kinds: # 모든 보석 구매 --> left 늘려서 최소구간 찾기
            if answer[1] - answer[0] > right - left: # 기존 구간 > 현재 구간
                answer = [left+1, right+1]           # left, right는 index
            
            bought[gems[left]] -= 1
            if bought[gems[left]] == 0:
                del bought[gems[left]]
            left += 1
            
        else:  # 보석 아직 부족 --> right 늘려서 보석 더 구매
            right += 1
            if right == len(gems):
                break
            bought[gems[right]] += 1
    
    return answer