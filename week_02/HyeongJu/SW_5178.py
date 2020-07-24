import sys

sys.stdin=open('sample_input5178.txt','r')

class Tree:
    def __init__(self,N):
        self.tree=[0]*(N+1) #initialize the tree with zeros

    def insert(self,i,v): #index, value
        self.tree[i]=v

    def sum_leaf(self,N):
        for i in range(len(self.tree)-1,0,-1): #from max index to 1
            if self.tree[i]==0:
                try: #sum of left child and right child
                    self.tree[i]=self.tree[i*2]+self.tree[(i*2)+1]
                    
                except IndexError: #there is no right child
                    self.tree[i]=self.tree[i*2]
                    
    def return_value(self,L):
        return self.tree[L]
                
T=int(input())

for test_case in range(1,T+1):
    
    N,M,L=map(int,input().split())
    
    tree=Tree(N)

    for _ in range(M):
        index,value=map(int,input().split())
        tree.insert(index,value)
        
    tree.sum_leaf(N)
    
    print("#{} {}".format(test_case,tree.return_value(L)))
    
