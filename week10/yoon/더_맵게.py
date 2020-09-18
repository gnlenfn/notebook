import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:                              # 최소값이 K보다 큰 경우 break --> 완성
        if len(scoville) == 1 and scoville[0] < K:      # heap의 길이가 1인데 원소가 여전히 K보다 작다 --> 실패
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)    # heap의 첫 번째, 두 번째 요소를 pop하고 연산하여 push
        answer += 1                                     # push가 일어날 때 마다 횟수가 1씩 증가
    return answer

print(solution([0,0,1,2,3], 30))