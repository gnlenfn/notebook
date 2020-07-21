import sys

sys.stdin=open('sample_input5122.txt','r')

##################################################################
#example

#I 2 7 -> 2번 인덱스 앞에 7을 추가하고, 한 칸 씩 뒤로 이동한다.
#D 4 -> 4번 인덱스 자리를 지우고, 한 칸 씩 앞으로 이동한다.
#C 3 8 -> 3번 인덱스 자리를 8로 바꾼다.

##################################################################

def edit_array(m,l):
    
    array=list(map(int,input().split()))

    for _ in range(m):
        
        edit=list(input().split())
        #print("edit rule:",edit)
        
        if edit[0]=='I': #Insert
            array.insert(int(edit[1]),int(edit[2]))
            
        elif edit[0]=='D': #Delete
            del array[int(edit[1])]
            
        elif edit[0]=='C': #Change
            array[int(edit[1])]=int(edit[2])
                
    #print(array)
            
    try:
        return array[l]
    except IndexError:
        return -1

T=int(input())

for test_case in range(1,T+1):
    
    N,M,L=list(map(int,input().split()))
    result=edit_array(M,L)
    
    print("#{} {}".format(test_case,result))
    
