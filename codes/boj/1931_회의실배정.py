def solution(arr):
    start_time = 0
    arr.sort()                      # 시작시간 기준 정렬
    arr.sort(key=lambda x : x[1])   # 종료시간 기준 정렬
    count = 0
    stack = []
    for time in arr:
        start, end = time
        if start >= start_time:
            count += 1
            start_time = end
    return count

tc = int(input())

meetings = []
for _ in range(tc):
    start, end = map(int, input().split())
    meetings.append((start, end))

print(solution(meetings))

 