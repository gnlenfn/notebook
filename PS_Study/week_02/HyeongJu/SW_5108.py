import sys

sys.stdin=open("sample_input5108.txt","r")

T=int(input())

for test_case in range(1,T+1):
    
    N,M,L=map(int,input().split())
    
    array=[i for i in map(int,input().split())]
    #print(array)
    
    for i in range(M):
        index,num=map(int,input().split())
        array.insert(index,num) #array index에 num을 추가
        
    print("#{} {}".format(test_case,array[L]))
