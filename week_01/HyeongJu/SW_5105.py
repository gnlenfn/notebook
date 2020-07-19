import sys

sys.stdin=open('sample_input5105.txt','r')

def BFS(x,y):
    #상 우 하 좌
    x_axis=[0,1,0,-1]
    y_axis=[1,0,-1,0]

    global distance

    #시작지점 저장
    stack.append((y,x))
    queue.append((y,x))

    #큐가 비어있기 전까지
    while queue:

        y,x=queue.pop(0)
        
        for i in range(4):
            
            next_x=x+x_axis[i]
            next_y=y+y_axis[i]

            #방문하지 않았거나, 범위를 벗어나지 않거나, 벽이 아닌경우
            if (next_y,next_x) not in stack and (0<=next_x<N and 0<=next_y<N) and maze[next_y][next_x] !=1:
                stack.append((next_y,next_x))
                queue.append((next_y,next_x))
                #print("stack:",stack)
                #print("queue:",queue)
                
                distance_save[next_y][next_x] = distance_save[y][x] +1
                #print(distance_save)
                
                if maze[next_y][next_x]==3:
                    distance=distance_save[next_y][next_x]-1 #시작지점은 제외
                    return

                    
T=int(input())

for test_case in range(1,T+1):
    
    N=int(input())
    
    maze=[list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                y_start=i
                x_start=j

    stack=[]
    queue=[]

    #거리를 저장할 빈 matrix 생성
    distance_save=[[0]*N for _ in range(N)]
    distance=0

    BFS(x_start,y_start)

    print('#{} {}'.format(test_case,distance))
