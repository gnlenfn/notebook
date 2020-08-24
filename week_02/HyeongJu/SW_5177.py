import sys

sys.stdin=open('sample_input5177.txt','r')

class Heap:
    def __init__(self,N):
        self.heap=[0]*(N+1)

    def insert(self,i,v):
        
        self.heap[i]=v
        
        if self.heap[i//2]>self.heap[i]: #parent>child
            
            #self.heap[i]=self.heap[i//2] #swap parent and child
            #self.heap[i//2]=v
            self.heap[i],self.heap[i//2]=self.heap[i//2],self.heap[i]

        #print(self.heap)

    def return_value(self,N):
        
        result=0
        
        while N!=0:
            result+=self.heap[N//2] #sum ancestors
            N=N//2
            
        return result
        
T=int(input())

for test_case in range(1,T+1):
    
    N=int(input())
    
    value_list=list(map(int,input().split()))

    heap=Heap(N)

    for index in range(len(value_list)):
        value=value_list[index]
        heap.insert(index+1,value)
        
    #print()
    print('#{} {}'.format(test_case,heap.return_value(N)))

#####수정 필요!!#####
    
