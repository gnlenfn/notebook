from itertools import combinations
def solution(numbers):
    answer = []
    stat = set(map(sum, combinations(numbers, 2)))
    
    return sorted(list(stat))