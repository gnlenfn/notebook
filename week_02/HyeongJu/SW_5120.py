import sys

sys.stdin=open('sample_input5120.txt','r')


def make_password(m,k):

    array=list(map(int,input().split()))

    start=0
    
    for _ in range(k):
        
        start=start+m #m씩 이동

        if len(array)>start:
            array.insert(start,array[start-1]+array[start])
            
        elif len(array)==start:
            #array.insert(start,array[start-1]+array[0])
            array.append(array[-1]+array[0])
            
        elif len(array)<start:
            #array.insert(start-len(array),array[start-len(array)-1]+array[start-len(array)])
            start=start-len(array)
    
    return array
         

T=int(input())

for test_case in range(1,T+1):
    
    N,M,K=list(map(int,input().split()))

    password=list(reversed(make_password(M,K)))

    print("#{}".format(test_case),end=' ')
    print(*password[:10])

#####뭐가 틀린걸까..?#####
