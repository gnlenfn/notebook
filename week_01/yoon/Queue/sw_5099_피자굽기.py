T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split()) # n: size of oven, m: number of pizza
    cheese = list(map(int, input().split()))

    oven = []
    for i in range(m):
        cheese[i] = [i+1, cheese[i]]

    for i in range(n):
        oven.append(cheese.pop(0))
    move = 0                        # oven 몇 칸 이동?
    end = []                        # 몇 칸 이동했는지 체크
    while True:
        if oven[move][1] >> 1:      # cheeze가 0이 아니면    oven[move][1] // 2
            oven[move][1] = oven[move][1] >> 1
        else:                       
            if cheese:              # oven의 치즈가 0이면서 아직 오븐에 넣지 않은 피자가 남았을때
                oven[move] = cheese.pop(0)
            else:
                if move not in end:
                    end.append(move)
                    if len(end) == n:
                        result = oven[move][0]
                        break
        move += 1
        if move == n :
            move = 0
        
    print(f'#{test_case} {result}')

