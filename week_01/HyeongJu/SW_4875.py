import sys

sys.stdin=open('sample_input4875.txt','r')

def DFS(x,y):
    #상 우 하 좌
    x_axis=[0,1,0,-1]
    y_axis=[1,0,-1,0]
    
    global arrival

    #목적지에 도착했을 시 1을 리턴
    if maze[y][x]==3:
        arrival=1
        return

    stack.append((y,x))

    for i in range(4):
        
        next_x=x+x_axis[i]
        next_y=y+y_axis[i]

        #방문하지 않았거나, 범위를 벗어나지 않거나, 벽이 아닌경우
        if (next_y,next_x) not in stack and (0<=next_x<N and 0<=next_y<N) and maze[next_y][next_x]!=1:
            DFS(next_x,next_y)
            #print(stack)

        
T=int(input())

for test_case in range(1,T+1):
    
    N=int(input())
    
    maze=[list(map(int,list(input()))) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                x_start=j
                y_start=i
    
    #방문한 곳을 스택에 저장
    stack=[]
    
    arrival=0

    DFS(x_start,y_start)

    print("#{} {}".format(test_case,arrival))
