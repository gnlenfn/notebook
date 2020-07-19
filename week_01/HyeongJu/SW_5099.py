import sys
sys.stdin=open('sample_input5099.txt','r')

T = int(input())

for test_case in range(1,T+1):
    
    #N=화덕의 크기 M=피자 개수
    N,M=map(int,input().split())
    
    pizza_list=list(map(int,input().split()))

    queue=[]
    pizza_add=0
    
    for i in range(N):
        queue.append([pizza_list[pizza_add],pizza_add]) #[cheeze, number]
        pizza_add+=1
    #현재의 pizza_add = N
        
    #print(queue)
        
    #피자가 하나 남을때까지
    while len(queue)!=1:

        #cheeze check
        queue[0][0]=queue[0][0]//2
        
        if queue[0][0]==0:
            queue.pop(0)
            
            if pizza_add!=len(pizza_list):
                queue.append([pizza_list[pizza_add],pizza_add])
                pizza_add+=1
                
        #첫번째 피자의 치즈가 다 녹지 않았을 경우, 다음 피자 확인
        else:
            queue.append(queue.pop(0))

    #마지막으로 남은 피자의 번호 출력
    final=queue[0][1]+1
    print("#{} {}".format(test_case,final))
            
            
    
