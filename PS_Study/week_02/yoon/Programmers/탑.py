def solution(heights):
    answer = [0] * len(heights)
    
    for i in range(len(heights)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break
    return answer

"""
1. 높이가 같은 탑은 수신 안함
2. Stack 인 것 같은데 stack을 쓴다면?

O(N^2) 보다 복잡도가 낮은 풀이가 있나?

"""

print(solution([6,9,5,7,4]))