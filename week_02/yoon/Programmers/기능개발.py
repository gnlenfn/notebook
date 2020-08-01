def solution(progresses, speeds):
    answer = []
    while progresses:      
        for i in range(len(progresses)):
            progresses[i] += speeds[i]                  # progresses에 speeds만큼 더한다
        c = 0
        while progresses and progresses[0] >= 100:      # progresses의 값이 100이 넘으면 pop하고 카운트
            progresses.pop(0)                           # 앞의 기능이 먼저 출시되어야 뒤의 기능이 유효하기 때문에
            speeds.pop(0)                               # progresses[0]을 체크한다
            c += 1
        if c:                                           # 한 번에 출시되는 기능 수 check
            answer.append(c)
    return answer


solution([93,30,55], [1,30,5])